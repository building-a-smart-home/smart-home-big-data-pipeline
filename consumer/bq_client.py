from google.cloud import bigquery
from google.oauth2 import service_account
from .config import BQ_CREDENTIALS_FILE

# Create BQ credentials object
credentials = service_account.Credentials.from_service_account_file(BQ_CREDENTIALS_FILE)

# Construct a BigQuery client object
bq_client = bigquery.Client(credentials=credentials)
