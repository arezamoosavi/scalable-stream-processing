#!/bin/sh


set -o errexit
set -o nounset

celery worker --app=celery_app.app:app -l DEBUG -O fair --pool=eventlet --concurrency=2


exec "$@"
