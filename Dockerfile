FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

RUN apt-get update
# Architecture dependent packages - support for M1 Macs
RUN /bin/bash -c 'arch=$(arch | sed s/aarch64/arm64/); if [[ "$arch" == "arm64" ]]; then apt-get install libc6-arm64-cross -y --no-install-recommends; else apt-get install libc6-i386 -y --no-install-recommends; fi'

COPY ./requirements.txt /
RUN --mount=type=cache,target=/root/.cache/pip pip install -r /requirements.txt

# Volume added by docker-compose
WORKDIR /app
