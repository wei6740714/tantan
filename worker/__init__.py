
import os
import time

from celery import Celery
from django.conf import settings

from worker import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tantan.settings")

app = Celery('tantan')
app.config_from_object(config)

app.autodiscover_tasks(settings.INSTALLED_APPS)

def call_by_worker(func):
    task=app.task(func)
    return task.delay

@call_by_worker
def sendmail():
    time.sleep(2)
    print('mail sent.')
    open('D:/temp', 'w+')


