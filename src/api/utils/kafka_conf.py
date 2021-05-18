import logging
import os, json
from kafka import KafkaProducer

kafka_server = os.getenv("KAFKA_BOOTSTRAP_SERVER").split(";")
producer = KafkaProducer(
    bootstrap_servers=kafka_server,
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)


def produce_data(topic_name: str, data_obj):

    producer.send(topic_name, value=data_obj)
    producer.flush()
