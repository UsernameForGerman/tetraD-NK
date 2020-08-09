FROM python:3.6.11-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
  # psycopg2 dependencies
  && apt-get install gcc -y \
  && apt-get install libpq-dev -y
  # for Django translations
  # && apt-get install gettext -y

RUN addgroup --system telegram \
    && adduser --system --group telegram --shell /bin/sh

WORKDIR /home/telegram/

RUN mkdir -p /var/telegram/static/
RUN mkdir -p /var/telegram/media/

# Requirements are installed here to ensure they will be cached.
COPY ./telegram/requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt \
    && rm -rf /requirements

COPY ./deploy/production/telegram/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint
RUN chown telegram /entrypoint

COPY ./deploy/production/telegram/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start
RUN chown telegram /start

COPY ./deploy/production/telegram/celery/worker/start /start-celeryworker
RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker
RUN chown telegram /start-celeryworker

#COPY ./deploy/production/cms/celery/beat/start /start-celerybeat
#RUN sed -i 's/\r//' /start-celerybeat
#RUN chmod +x /start-celerybeat
#RUN chown django /start-celerybeat
#
#COPY ./deploy/production/cms/celery/flower/start /start-flower
#RUN sed -i 's/\r//' /start-flower
#RUN chmod +x /start-flower
COPY ./telegram /telegram

RUN chown -R telegram /telegram
RUN chown -R telegram /var/telegram/static
RUN chown -R telegram /var/telegram/media
# RUN chown -R django:django /home/django/
# RUN chown -R django:django /var/komax_site
# RUN mkdir /var/komax_site/admin
# RUN chown -R django:django /var/komax_site/admin
# RUN chmod +x /app/static
# RUN chmod +x /var/komax_site

RUN chown -R telegram /var/run/celery/
RUN chown -R telegram /var/log/celery/

USER telegram

WORKDIR /telegram

ENTRYPOINT ["/entrypoint"]