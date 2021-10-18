# syntax=docker/dockerfile:1
FROM python:3.7
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD gunicorn oc_lettings_site.wsgi
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

