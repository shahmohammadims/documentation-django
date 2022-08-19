FROM python:alpine

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip install --upgrade pip
RUN pip install -r requirments.txt
CMD python manage.py makemigrations users documentation; \
    while ! python manage.py migrate --no-input; do sleep 1; done; \
    python manage.py collectstatic --no-input; \
    gunicorn --bind :8000 config.wsgi:application
