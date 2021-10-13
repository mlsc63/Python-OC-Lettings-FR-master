# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONUNBUFFERED 1
ENV ALLOWED_HOSTS=127.0.0.1,[::1],0.0.0.0,.herokuapp.com


WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD gunicorn oc_lettings_site.wsgi:application