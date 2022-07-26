FROM python:3.10-slim as builder

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt


FROM python:3.10-slim

WORKDIR /app

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
# Set Python path to workdir
ENV PYTHONPATH=/app

COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*

COPY alembic.ini .

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# Id 1000 is used due to broken permissions for alembic migration files, 
RUN adduser -u 1000 --disabled-password --gecos "" --no-create-home appuser && chown -R appuser /app
USER appuser

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
