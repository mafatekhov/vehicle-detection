FROM python:3.9-slim-buster

WORKDIR /usr/src/ObjectDetectionBE

RUN apt-get update \
    && apt-get -y install gcc

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY ./start_server.sh /usr/src/ObjectDetectionBE/start_server.sh

RUN chmod +x /usr/src/ObjectDetectionBE/start_server.sh

COPY . .