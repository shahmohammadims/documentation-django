FROM python:alpine
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_PASSWORD=admin
RUN mkdir /api
WORKDIR /api
ADD . /api
RUN pip install --upgrade pip
RUN pip install -r requirments.txt

CMD python manage.py makemigrations documentation users --no-input; \
    while ! python manage.py migrate --no-input; do sleep 1; done; \
    python manage.py createsuperuser --email admin@admin.com --username admin --first_name super --last_name user --no-input; \
    python manage.py collectstatic --no-input; \
    gunicorn --bind 0.0.0.0:8000 config.wsgi:application