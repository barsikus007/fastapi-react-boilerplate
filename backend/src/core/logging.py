import logging

import orjson
import structlog


def uvicorn_color_message_remover(_, __, event_dict: structlog.types.EventDict) -> structlog.types.EventDict:
    if not event_dict["logger"].startswith("uvicorn"):
        return event_dict
    event_dict.pop("color_message", None)
    return event_dict


def configure_default_logging(
    shared_processors: list[structlog.types.Processor],
    logs_render: structlog.types.Processor,
    logging_level: int,
) -> None:
    formatter = structlog.stdlib.ProcessorFormatter(
        foreign_pre_chain=shared_processors,
        processors=[
            structlog.stdlib.ProcessorFormatter.remove_processors_meta,
            uvicorn_color_message_remover,
            logs_render,
        ],
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    for logger_name in [None, "uvicorn", "uvicorn.access", "sqlalchemy.engine.Engine"]:
        _logger = logging.getLogger(logger_name)
        # print(f"⚡🐍 {logger_name=}")
        # print(f"⚡🐍 {_logger.handlers=}")
        _logger.handlers.clear()
        _logger.addHandler(handler)
        _logger.setLevel(logging_level)


def configure_logger(*, logging_level: int = logging.INFO, is_production: bool = True):
    # structlog.stdlib.recreate_defaults()
    stdlib_processors = [
        structlog.stdlib.add_logger_name,
        structlog.stdlib.ExtraAdder(),
        structlog.stdlib.PositionalArgumentsFormatter(),
    ]
    common_processors = [
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        ## structlog.dev.set_exc_info,
        structlog.contextvars.merge_contextvars,
    ]
    development_processors = [
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M.%S", utc=False),
        structlog.dev.ConsoleRenderer(colors=True),
    ]
    production_processors = [
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.dict_tracebacks,
        structlog.processors.CallsiteParameterAdder(
            {
                structlog.processors.CallsiteParameter.PATHNAME,
                structlog.processors.CallsiteParameter.FILENAME,
                structlog.processors.CallsiteParameter.MODULE,
                structlog.processors.CallsiteParameter.FUNC_NAME,
                structlog.processors.CallsiteParameter.THREAD,
                structlog.processors.CallsiteParameter.THREAD_NAME,
                structlog.processors.CallsiteParameter.PROCESS,
                structlog.processors.CallsiteParameter.PROCESS_NAME,
            },
        ),
        structlog.processors.JSONRenderer(serializer=lambda *a, **kw: orjson.dumps(*a, **kw).decode()),
    ]

    # is_production = True
    *shared_processors, logs_render = [
        *common_processors,
        *(production_processors if is_production else development_processors),
    ]
    structlog.configure(
        processors=[
            *shared_processors,
            logs_render,
            # structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        # wrapper_class=structlog.stdlib.BoundLogger,
        wrapper_class=structlog.make_filtering_bound_logger(logging_level),
        # logger_factory=structlog.stdlib.LoggerFactory(),
        # logger_factory=structlog.BytesLoggerFactory(),
        cache_logger_on_first_use=True,
    )

    configure_default_logging([*stdlib_processors, *shared_processors], logs_render, logging_level)
