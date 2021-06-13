# -*- coding: utf-8 -*-

import os
import io
import time
import json
import logging
import traceback

from celery import current_task
from celery.signals import setup_logging
from .app import app as celery_app

from log_setup import setup_custom_logger

# setup celery logger
setup_logging.connect(setup_custom_logger)

logger = setup_custom_logger("root")
logger.info("celery running!")


@celery_app.task(name="test_pen", default_retry_delay=30 * 60, retry_backoff=5, retry_kwargs={'max_retries': 10, 'countdown': 10}, soft_time_limit=6000)
def queue_func(data_json):
    
    logger.info(
        "user_id: " + data_json["user_id"] +
        " cur_time: " + data_json["cur_time"]
    )

    k = 0
    for i in range(50):
        k += 2 ** i

    return data_json
