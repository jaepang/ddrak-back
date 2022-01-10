FROM python:3
ENV PYTHONUNBUFFERED 1

ARG ALLOWED_HOSTS
ARG SECRET_KEY
ARG CORS_ORIGIN_WHITELIST

ENV ALLOWED_HOSTS $DJANGO_ALLOWED_HOSTS
ENV SECRET_KEY $DJANGO_SECRET_KEY
ENV CORS_ORIGIN_WHITELIST $DJANGO_CORS_ORIGIN_WHITELIST
CMD echo ALLOWED_HOSTS SECRET_KEY CORS_ORIGIN_WHITELIST

RUN mkdir /ddrak-back
WORKDIR /ddrak-back
COPY requirements.txt /ddrak-back/
EXPOSE 8000
RUN pip install -r requirements.txt
COPY . /ddrak-back/
RUN python manage.py makemigrations --settings=ddrakapi.config.settings.debug
RUN python manage.py migrate --settings=ddrakapi.config.settings.debug