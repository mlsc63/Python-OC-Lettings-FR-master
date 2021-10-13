# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
#RUN python manage.py collectstatic --noinput --clear
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT