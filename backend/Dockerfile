ARG PYTHON_VERSION=3.10.11
FROM python:${PYTHON_VERSION}-slim as builder

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    # pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt
    pip wheel --no-deps --wheel-dir /wheels -r requirements.txt


FROM python:${PYTHON_VERSION}-slim

WORKDIR /app

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1
# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1
# Set Python path to workdir
ENV PYTHONPATH=/app

COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*

COPY alembic.ini .

# Id 1000 is used instead of 10001 due to broken permissions for alembic migration files,
ARG UID=10001
ARG USER=appuser
# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    $USER && chown -R $USER /app
USER $USER

EXPOSE 8000

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
