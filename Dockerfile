FROM python:3
ENV PYTHONUNBUFFERED 1

ARG DJANGO_ALLOWED_HOSTS
ARG DJANGO_SECRET_KEY
ARG DJANGO_CORS_ORIGIN_WHITELIST
ARG DB_NAME
ARG DB_PASSWORD

ENV ALLOWED_HOSTS=$DJANGO_ALLOWED_HOSTS \
    SECRET_KEY=$DJANGO_SECRET_KEY \
    CORS_ORIGIN_WHITELIST=$DJANGO_CORS_ORIGIN_WHITELIST \
    DB_NAME=$DB_NAME \
    DB_PASSWORD=$DB_PASSWORD
RUN echo $ALLOWED_HOSTS $SECRET_KEY $CORS_ORIGIN_WHITELIST $DB_NAME $DB_PASSWORD

RUN mkdir /ddrak-back
WORKDIR /ddrak-back
COPY requirements.txt /ddrak-back/
EXPOSE 8000
RUN pip install -r requirements.txt
COPY . /ddrak-back/
RUN python manage.py makemigrations --settings=ddrakapi.config.settings.deploy
RUN python manage.py migrate --settings=ddrakapi.config.settings.deploy