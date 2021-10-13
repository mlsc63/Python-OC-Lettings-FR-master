# syntax=docker/dockerfile:1
FROM python:3.7
#set environment variables
ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

#set work directory
WORKDIR /code

#Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# copy project
COPY . /code/