FROM python:3.5
MAINTAINER Lmorillas <morillas@gmail.com>

RUN mkdir -p /usr/api
COPY ./app/* /usr/api/
WORKDIR /usr/api

#RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENV PORT 5000
EXPOSE  $PORT

#CMD ["python", "-u", "arasaac.py"]
 ENTRYPOINT gunicorn --bind 0.0.0.0:5000 arasaac:app