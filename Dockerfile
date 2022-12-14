FROM python:3.9.13-slim-buster
RUN mkdir -p /opt/services/djangoapp/src
RUN apt update
RUN apt-get install -y libpq-dev python-dev gcc
WORKDIR /opt/services/djangoapp/src
COPY ./requirements.txt /opt/services/djangoapp/src/
RUN pip install --upgrade -r /opt/services/djangoapp/src/requirements.txt
COPY ./ /opt/services/djangoapp/src