FROM python:alpine

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip install --upgrade pip
RUN pip install -r requirments.txt
CMD while ! python manage.py migrate --no-input; do sleep 1; done; \
    gunicorn --bind :8000 config.wsgi:application