"""Module that is for config of the path and logging."""
from datetime import datetime
import os
import re

LOG_DIR = "/var/log/remote/aide" # Define log directory and output CSV file
CSV_DIR = "/public/"
CSV_FILE = os.path.join(CSV_DIR, f"aide_logs_{datetime.now().strftime('%Y%m%d')}.csv")

# Define regex eo extract required log data
LOG_PATTERN = re.compile(r'(\w+ \d+ \d+:\d+:\d+) (\S+) aide: Start timestamp: (.+)')

LIST_OF_LOGS = []
