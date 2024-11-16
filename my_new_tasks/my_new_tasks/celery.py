
from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_new_tasks.settings')
QUEUE_NAME = ''
app = Celery('my_new_tasks')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
