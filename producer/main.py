from confluent_kafka import Producer
import json
from .config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
from .logger import logger

producer = Producer({'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS})
log = logger()

def receipt(err, msg):
    if err is not None:
        log.error(f'Failed to deliver message: {err}')
    else:
        message = f'Produced message on topic {msg.topic()} with value of {msg.value().decode("utf-8")}'
        log.info(message)
        print(message)

def send_data(data):
    message = json.dumps(data).encode('utf-8')
    producer.produce(KAFKA_TOPIC, message, callback=receipt)
    producer.poll(1)
    producer.flush()
