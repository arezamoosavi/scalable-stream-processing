FROM python:3.7-slim-buster

ENV PYTHONIOENCODING=utf-8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements/faust.txt requirements.txt
RUN pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt \
  && rm -rf requirements.txt

RUN mkdir -p /main
COPY ./src/stream /main

# Faust
COPY ./dockers/stream/faust_run.sh /faust_run.sh
RUN chmod a+rwx /faust_run.sh \
  && chmod -R a+rwx /main

WORKDIR /main