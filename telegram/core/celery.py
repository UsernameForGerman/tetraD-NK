from __future__ import absolute_import

from django.conf import settings
from django.apps import AppConfig, apps

import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.local')


app = Celery("telegram")
# Using a string here means the worker will not have to
# pickle the object when using Windows.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object("django.conf:settings", namespace="CELERY")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks()

# class CeleryAppConfig(AppConfig):
#     name = "telegram.core"
#     verbose_name = "Celery Config"
#
#     def ready(self) -> None:
#         installed_apps = [app_config.name for app_config in apps.get_app_configs()]
#         app.autodiscover_tasks(lambda: installed_apps, force=True)


@app.task(bind=True)
def debug_task(self) -> None:
    print(f"Request: {self.request!r}")  # pragma: no cover


celery_inspector = app.control.inspect()