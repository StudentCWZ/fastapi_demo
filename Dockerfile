FROM python:3.11-slim

LABEL name="app"
LABEL version="0.1.0"
LABEL description="FastAPI Demo"

# System deps:
ENV TZ=Asia/Shanghai \
    PIPURL="https://pypi.tuna.tsinghua.edu.cn/simple" \
    POETRY_HOME=/opt/poetry \
    POETRY_VENV=/opt/poetry-venv \
    POETRY_CACHE_DIR=/opt/.cache \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TF_CPP_MIN_LOG_LEVEL=3

# Install poetry separated from system interpreter
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    python3 -m venv $POETRY_VENV && \
    $POETRY_VENV/bin/pip install -U pip setuptools && \
    $POETRY_VENV/bin/pip install poetry

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Copy folder them in docker layerz
WORKDIR /usr/src/fastapi-demo
COPY . /usr/src/fastapi-demo/

# Project initialization:
RUN chmod +x docker-entrypoint.sh && \
    poetry install --no-interaction --no-ansi

# Run the application:
CMD ["./docker-entrypoint.sh"]
