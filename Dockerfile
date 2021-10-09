FROM python:3
ENV PYTHONUNBUFFERED=1
    PYTHONDONTWRITEBYTECODE=1 \
    DEBUG=0 \
    PORT=8000 \
    SENTRY_DSN=https://11111111111111111111111111111111@o555555.ingest.sentry.io/5555555


WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
