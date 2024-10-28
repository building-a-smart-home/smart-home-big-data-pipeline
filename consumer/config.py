import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# BigQuery configuration
BQ_CREDENTIALS_FILE = 'credentials/bq-service-account.json'
BQ_TABLE_ID = os.getenv('BQ_TABLE_ID')

# Kafka configuration
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_GROUP_ID = 'smart-home-consumer'
KAFKA_TOPIC = 'sensor_data'
