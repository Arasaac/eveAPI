FROM python:latest

WORKDIR /code/

RUN pip3 install --upgrade pip

RUN pip3 install  eve

EXPOSE 5000

ADD ./app/* /code/
COPY ./app/* /code/


