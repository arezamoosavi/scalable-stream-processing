import logging
import os
import json
import random
from kafka import KafkaProducer

kafka_server = os.getenv("KAFKA_BOOTSTRAP_SERVER").split(";")
producer = KafkaProducer(
    bootstrap_servers=kafka_server,
    key_serializer=lambda x: x.encode("utf-8"),
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
    acks='all',
    retries=5,
    compression_type=None,
)


def on_send_success(record_metadata):
    print(record_metadata.partition)
    # print(record_metadata.topic)
    # print(record_metadata.partition)
    # print(record_metadata.offset)


def on_send_error(excp):
    print('I am an errback')
    # handle exception


def produce_data(topic_name: str, msg_value):
    key_msg = str(random.choice([i for i in range(50)]))
    producer.send(topic_name, key=key_msg, value=msg_value).add_callback(
        on_send_success).add_errback(on_send_error)
    producer.flush()
