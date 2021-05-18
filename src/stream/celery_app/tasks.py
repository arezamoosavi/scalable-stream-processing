# -*- coding: utf-8 -*-

import os, io, time, json
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


@celery_app.task(name="test_pen")
def just_do_test(data_json):

    logger.info("data is here!")
    k = 0
    for i in range(100):
        k += 10 ** i
    logger.info("k: " + str(k))

    return data_json
