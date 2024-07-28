import os
import csv
import re
from datetime import datetime, timedelta

# Define log directory and output CSV file
LOG_DIR = "/var/log/remote/aide"
CSV_DIR = "/path/to/csv"
CSV_FILE = os.path.join(CSV_DIR, f"aide_logs_{datetime.now().strftime('%Y%m%d')}.csv")

# Define regex to extract required log data
log_pattern = re.compile(r'(\w+ \d+ \d+:\d+:\d+) (\S+) aide: Start timestamp: (.+)')

def extract_logs(log_dir):
    logs = []
    for root, _, files in os.walk(log_dir):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                for line in f:
                    match = log_pattern.search(line)
                    if match:
                        log_time, server, timestamp = match.groups()
                        logs.append({
                            "log_time": log_time,
                            "server": server,
                            "timestamp": timestamp
                        })
    return logs

def transform_to_csv(logs, csv_file):
    fieldnames = ["log_time", "server", "timestamp"]
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for log in logs:
            writer.writerow(log)

def main():
    logs = extract_logs(LOG_DIR)
    transform_to_csv(logs, CSV_FILE)

if __name__ == "__main__":
    main()
