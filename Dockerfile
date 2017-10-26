FROM python:3.6

RUN apt-get update && \
    apt-get install -y && \
    apt-get install -y apache2