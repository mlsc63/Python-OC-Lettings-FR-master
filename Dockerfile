# syntax=docker/dockerfile:1
FROM python:3.7
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN python manage.py collectstatic --noinput
CMD gunicorn --bind 0.0.0.0:$PORT config.wsgi


