import csv
from datetime import datetime
from .config import MEASUREMENTS_DIR
import requests

def get_csv_files_in_github():
    """Fetches a list of .csv file paths from the specified GitHub repository folder."""
    url = f"{MEASUREMENTS_DIR}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    files = response.json()

    # Filter for CSV files and get their download URLs
    csv_files = [file for file in files if file['name'].endswith('.csv')]
    return csv_files

def read_csv_file_from_url(url):
    """Reads CSV content from a URL and formats it as a list of dictionaries."""
    response = requests.get(url)
    response.raise_for_status()
    content = response.content.decode('utf-8').splitlines()
    reader = csv.reader(content, delimiter='\t')
    data = []
    for row in reader:
        timestamp, value = row
        data.append({
            "timestamp": datetime.fromtimestamp(int(timestamp)).isoformat(),
            "value": float(value) if '.' in value else int(value)
        })
    return data

def get_sensor_data():
    """Retrieves and processes sensor data from CSV files in the GitHub repository."""
    sensor_data = []
    csv_files = get_csv_files_in_github()

    for file in csv_files:
        filename = file['name']
        room, sensor_type = filename.replace('.csv', '').split('_', 1)
        readings = read_csv_file_from_url(file['download_url'])

        # Add room and sensor type info to each data entry
        for reading in readings:
            reading.update({"room": room, "sensor_type": sensor_type})
            sensor_data.append(reading)
    return sensor_data
