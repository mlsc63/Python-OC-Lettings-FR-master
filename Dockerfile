# syntax=docker/dockerfile:1
FROM python:3.7
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT -e DJANGO_SETTINGS_MODULE=oc_lettings_site.settings.local