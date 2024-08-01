"""Main module saves AIDE logs into path"""
import os
import csv
import re
from datetime import datetime

LOG_DIR = "/var/log/remote/aide" # Define log directory and output CSV file
LOG_DIR = "/var/log/remote/aide"
CSV_DIR = "/path/to/csv"
CSV_FILE = os.path.join(CSV_DIR, f"aide_logs_{datetime.now().strftime('%Y%m%d')}.csv")

# Define regex to extract required log data
log_pattern = re.compile(r'(\w+ \d+ \d+:\d+:\d+) (\S+) aide: Start timestamp: (.+)')


def extract_logs(log_dir: str, log_list: list) -> list:
    """Extracts logs from given diretory

    :param log_dir: str, path to directory.
    :param log_list: list, list of logs.
    :returns: list
    """
    for root, _, files in os.walk(log_dir):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                for line in f:
                    match = log_pattern.search(line)
                    if match:
                        log_time, server, timestamp = match.groups()
                        log_list.append({
                            "log_time": log_time,
                            "server": server,
                            "timestamp": timestamp
                        })
    return log_list


def transform_to_csv(log_list: list, csv_file: str) -> None:
    """Transforms logs to CSV format

    :param log_list: list, list of logs.
    :param csv_file: str, path to the csv file.
    :returns: None.
    """
    fieldnames = ["log_time", "server", "timestamp"]
    with open(csv_file, 'w', newline=' ') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for log in log_list:
            writer.writerow(log)

LIST_OF_LOGS = []

if __name__ == "__main__":
    logs = extract_logs(LOG_DIR, log_list=LIST_OF_LOGS)
    transform_to_csv(logs, CSV_FILE)
