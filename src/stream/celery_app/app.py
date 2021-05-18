from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")

app = Celery(
    "queue_app",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
    include=["celery_app.tasks",],
)

app.conf["task_acks_late"] = True
app.conf["worker_prefetch_multiplier"] = 1
