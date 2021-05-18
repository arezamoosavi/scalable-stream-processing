#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging
import logging.handlers

from datetime import datetime

LOGS_DIR = os.getenv("LOGS_DIR")
os.makedirs(LOGS_DIR, exist_ok=True)


def setup_custom_logger(name="root", **kw):
    # logger settings
    file_name = LOGS_DIR + "app_logs.log"

    log_format = "%(asctime)s | %(module)s | %(levelname)s | %(funcName)s | %(message)s"

    formatter = logging.Formatter(log_format)

    logging.basicConfig(filename=file_name, format=log_format, level=logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)

    logger.addHandler(handler)

    return logger
