FROM python:3
ENV PYTHONUNBUFFERED 1

ARG DJANGO_ALLOWED_HOSTS
ARG DJANGO_SECRET_KEY
ARG DJANGO_CORS_ORIGIN_WHITELIST

ENV DJANGO_ALLOWED_HOSTS $DJANGO_ALLOWED_HOSTS
ENV DJANGO_SECRET_KEY $DJANGO_SECRET_KEY
ENV DJANGO_CORS_ORIGIN_WHITELIST $DJANGO_CORS_ORIGIN_WHITELIST

RUN mkdir /ddrak-back
WORKDIR /ddrak-back
COPY requirements.txt /ddrak-back/
EXPOSE 8000
RUN pip install -r requirements.txt
COPY . /ddrak-back/
RUN python manage.py makemigrations --settings=ddrakapi.config.settings.debug
RUN python manage.py migrate --settings=ddrakapi.config.settings.debug