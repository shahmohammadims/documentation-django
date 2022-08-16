FROM python:alpine

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_PASSWORD=admin

RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip install --upgrade pip
RUN pip install -r requirments.txt

CMD python manage.py makemigrations account exercise payment --no-input; \
    while ! python manage.py migrate --no-input; do sleep 1; done; \
    python manage.py createsuperuser --email 09130000000 --username admin --first_name admin --last_name admin --no-input; \
    python manage.py collectstatic --no-input; \
    gunicorn --bind :8000 config.wsgi:application