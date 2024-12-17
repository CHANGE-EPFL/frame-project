# FastAPI
Based loosely on https://github.com/gauravgola96/FastAPI-Example

## Requirements
- python 3.10.9
- poetry
- Make
- Docker with docker compose
- OS:
  - Windows: docker desktop with wsl
  - Apple: with docker desktop dependencies installed via brew
  - Linux: libwebp-dev

## How to run

Run Locally
```
make install; make run
```

Swagger docs
```
http://localhost:8000/docs
```

To provide .env use Dockerfile.
```
Path : ./Dockerfile
```

## Install
Don't forget to install libwebp-dev on the machine (cf Dockerfile)
