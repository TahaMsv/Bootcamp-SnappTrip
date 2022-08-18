FROM python:3.9.13-slim-buster
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src
COPY ./requirements.txt /opt/services/djangoapp/src/
RUN pip install --upgrade -r /opt/services/djangoapp/src/requirements.txt
COPY ./ /opt/services/djangoapp/src
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--workers", "3", "snapptrip.wsgi"]
