FROM python:3.6.11-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
  # psycopg2 dependencies
  && apt-get install gcc -y \
  && apt-get install libpq-dev -y \
  # for Django translations
  && apt-get install gettext -y

WORKDIR /telegram

COPY ./telegram/requirements/ /requirements
RUN pip install -r /requirements/local.txt

COPY ./deploy/local/telegram/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./deploy/local/telegram/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

COPY ./telegram /telegram

ENTRYPOINT ["/entrypoint"]


