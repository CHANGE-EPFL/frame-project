FROM python:3.10.15-bullseye
ENV UV_VERSION=0.7.3
RUN pip install "uv==$UV_VERSION"
ENV PYTHONPATH="$PYTHONPATH:/app"

WORKDIR /app

COPY uv.lock pyproject.toml /app/
COPY start.sh /app/
COPY api /app/api

RUN uv pip install --system --no-cache-dir -e /app

ENTRYPOINT sh start.sh
