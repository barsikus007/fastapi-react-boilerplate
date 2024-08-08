# pin version to prevent side-effects when new lts version releases
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim AS installer

RUN --mount=from=ghcr.io/astral-sh/uv:latest,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    uv pip install --system -r requirements.txt


FROM installer AS base

ARG WORKDIR=/app
WORKDIR $WORKDIR

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1
# Set Python path to workdir
ENV PYTHONPATH=$WORKDIR

COPY alembic.ini pyproject.toml ./

EXPOSE 8000


FROM base AS development

CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0"]


FROM base AS production
ARG USER=python

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
ARG UID=10001
RUN useradd \
    --no-log-init \
    --no-create-home \
    --shell /sbin/nologin \
    --uid "${UID}" \
    $USER
USER $USER

COPY src/ src/
COPY alembic/ alembic/

ENV PRODUCTION=True

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "src.main:app", "-b", "0.0.0.0:8000", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]


FROM base AS debug

RUN --mount=from=ghcr.io/astral-sh/uv:latest,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system debugpy

EXPOSE 5678

CMD ["python", "-m", "debugpy", "--wait-for-client", "--listen", "0.0.0.0:5678", "-m", "uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0"]
