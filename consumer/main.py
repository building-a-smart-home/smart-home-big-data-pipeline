from confluent_kafka import Consumer
import ast
from .config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_GROUP_ID, KAFKA_TOPIC, BQ_TABLE_ID
from .bq_client import bq_client

# Create Kafka Consumer
consumer = Consumer({
    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
    'group.id': KAFKA_GROUP_ID,
    'auto.offset.reset': 'earliest'
})
print('Kafka Consumer has been initiated...')

# Subscribe to Kafka topic
consumer.subscribe([KAFKA_TOPIC])

def process_message():
    """Polls messages from Kafka and streams them into BigQuery."""
    msg = consumer.poll(timeout=1.0)
    if msg is None:
        return
    if msg.error():
        print(f'Error: {msg.error()}')
        return

    # Decode message and convert to dictionary
    data = msg.value().decode('utf-8')
    res = ast.literal_eval(data)
    print(res)

    # Stream data into BigQuery table
    rows_to_insert = [res]
    errors = bq_client.insert_rows_json(BQ_TABLE_ID, rows_to_insert)

    if not errors:
        print("New rows added.")
    else:
        print(f"Encountered errors while inserting rows: {errors}")

def close_consumer():
    """Closes the Kafka consumer."""
    consumer.close()
