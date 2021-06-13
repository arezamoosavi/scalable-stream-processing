import logging
import faust
from asyncio import sleep

import settings

from celery_app.app import app as celery_service

logger = logging.getLogger(__name__)

app = faust.App(
    id=settings.consumer_id,
    debug=settings.DEBUG,
    autodiscover=False,
    broker=settings.KAFKA_BOOTSTRAP_SERVER,
    store=settings.STORE_URI,
    topic_allow_declare=settings.TOPIC_ALLOW_DECLARE,
    topic_disable_leader=settings.TOPIC_DISABLE_LEADER,
    broker_credentials=settings.SSL_CONTEXT,
    consumer_auto_offset_reset="earliest",
    logging_config=settings.LOGGING,
)

pen_test_topic = app.topic(
    settings.topic_name, acks=settings.OFFSET_ACK_ON_KAFKA, partitions=None
)


@app.agent(pen_test_topic, concurrency=10)
async def process_pen_test_topic(stream):
    async for batch_event in stream.take(10, within=5):

        logger.info("the batch_event is: " + str(batch_event))

        results = [celery_service.send_task(
            "test_pen", (event,)) for event in batch_event]

        logger.info(
            f"process with token {[result.id for result in results]} is started!")

        await sleep(15)
