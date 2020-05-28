
from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from worker import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tantan.settings")

app = Celery('tantan')
print(config.result_cache_max)
app.config_from_object(config)
app.autodiscover_tasks(settings.INSTALLED_APPS)
# app.autodiscover_tasks()

def call_by_worker(func):
    task=app.task(func)
    return task.delay

# @call_by_worker
# def sendmail():
#     time.sleep(5)
#     print('mail sent.')

# import time
# from celery import Celery
#
# celery = Celery('tantan', broker='redis://127.0.0.1:6379/1')
#
# @celery.task
# def sendmail():
#     time.sleep(5)
#     print('mail sent.')
