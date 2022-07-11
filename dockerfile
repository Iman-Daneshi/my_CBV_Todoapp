FROM python:3.8-slim-buster

ENV PYTHONDONTWRITENBYTECODE=1
ENV PYTHONUNBUFFERRED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./core /app
