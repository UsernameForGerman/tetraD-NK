FROM python:3.6.11-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
  # psycopg2 dependencies
  && apt-get install gcc -y \
  && apt-get install libpq-dev -y
  # for Django translations
  # && apt-get install gettext -y

RUN addgroup --system django \
    && adduser --system --group django --shell /bin/sh

WORKDIR /home/django/

RUN mkdir -p  /home/django/app/
RUN mkdir -p  /home/django/app/static
RUN mkdir -p  /home/django/app/media
RUN mkdir -p  /var/tetrad/static/
RUN mkdir -p  /var/tetrad/media/

# Requirements are installed here to ensure they will be cached.
COPY ./tetrad_cms/requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt \
    && rm -rf /requirements

COPY ./deploy/production/cms/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint
RUN chown django /entrypoint

COPY ./deploy/production/cms/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start
RUN chown django /start

#COPY ./deploy/production/django/celery/worker/start /start-celeryworker
#RUN sed -i 's/\r//' /start-celeryworker
#RUN chmod +x /start-celeryworker
#RUN chown django /start-celeryworker

#COPY ./deploy/production/cms/celery/beat/start /start-celerybeat
#RUN sed -i 's/\r//' /start-celerybeat
#RUN chmod +x /start-celerybeat
#RUN chown django /start-celerybeat
#
#COPY ./deploy/production/cms/celery/flower/start /start-flower
#RUN sed -i 's/\r//' /start-flower
#RUN chmod +x /start-flower
COPY ./tetrad_cms /app

RUN chown -R django /app
RUN chown -R django /var/tetrad/static
RUN chown -R django /var/tetrad/media
# RUN chown -R django:django /home/django/
# RUN chown -R django:django /var/komax_site
# RUN mkdir /var/komax_site/admin
# RUN chown -R django:django /var/komax_site/admin
# RUN chmod +x /app/static
# RUN chmod +x /var/komax_site

USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint"]