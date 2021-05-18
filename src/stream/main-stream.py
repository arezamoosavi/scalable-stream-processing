import logging

import faust

from . import settings

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


@app.agent(pen_test_topic)
async def process_pen_test_topic(stream):
    async for event in stream:
        logger.info("the event is: " + str(event))

        logger.info("process done on: " + str(event))

        logger.info("event saved: " + str(event))

