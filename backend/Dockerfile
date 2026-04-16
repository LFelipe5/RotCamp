FROM python:3.13-slim
ENV PYTHONUNBUFFERED 1
ARG TZ='America/Fortaleza'
ARG PKG='build-essential python3-dev'

WORKDIR /app

COPY requirements.txt .
RUN set -x && \
    # configure timezone
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    # install deps
    apt-get update && \
    apt-get install -y ${PKG} && \
    # install django and deps
    python -m pip install --upgrade pip && \
    pip3 install -r requirements.txt --no-cache-dir --compile && \
    rm -f requirements.txt && \
    # clean container
    # apt-get remove -y ${PKG} && \
    apt-get autoremove -y && \
    apt-get clean


EXPOSE 8000
