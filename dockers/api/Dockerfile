FROM python:3.7-slim-buster

ENV PYTHONIOENCODING=utf-8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements/api.txt requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf requirements.txt

RUN mkdir -p /main
COPY ./ml_services /main

COPY ./compose/local/api/run_web.sh /run_web.sh
RUN chmod a+rwx /run_web.sh && chmod -R a+rwx /main

WORKDIR /main