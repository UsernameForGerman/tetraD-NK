FROM python:3.6.11-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
  # psycopg2 dependencies
  && apt-get install gcc -y \
  && apt-get install libpq-dev -y \
  # for Django translations
  && apt-get install gettext -y

WORKDIR /cms

COPY ./tetrad_cms/requirements/ /requirements
RUN pip install -r /requirements/local.txt

COPY ./deploy/local/cms/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./deploy/local/cms/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

COPY ./deploy/local/cms/celery/worker/start /start-celeryworker
RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./tetrad_cms /cms

ENTRYPOINT ["/entrypoint"]


