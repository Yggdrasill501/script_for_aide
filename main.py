"""Main module saves AIDE logs into path"""
import os
import csv
import logging

logging.basicConfig()

def extract_logs(log_dir: str, log_list: list, log_pattern: ) -> list | bool:
    """Extracts logs from given diretory

    :param log_dir: str, path to directory.
    :param log_list: list, list of logs.
    :returns: list
    """
    for root, _, files in os.walk(log_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try: 
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
            except FileNotFoundError:
                return False
    return log_list


def transform_to_csv(log_list: list, csv_file: str) -> None | bool:
    """Transforms logs to CSV format

    :param log_list: list, list of logs.
    :param csv_file: str, path to the csv file.
    :returns: None.
    """
    fieldnames = ["log_time", "server", "timestamp"]
    try:
        with open(csv_file, 'w', newline=' ') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for log in log_list:
                writer.writerow(log)
    except FileNotFoundError as error: 
# logging.error(msg=f"Tranforming csv failed because the desired path does not exist, exception: {error}")
        return False

LIST_OF_LOGS = []

if __name__ == "__main__":
    logs = extract_logs(LOG_DIR, log_list=LIST_OF_LOGS)
    transform_to_csv(logs, CSV_FILE)
