# AIDE Log Exporter
This project automates the process of exporting AIDE logs from Linux servers to a CSV file, which can be consumed by the Axonius CSV adapter.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Syslog-ng Configuration](#syslog-ng-configuration)
- [Scheduling the Script](#scheduling-the-script)
- [Axonius Connector Configuration](#axonius-connector-configuration)
- [Directory Structure](#directory-structure)
- [License](#license)

## Prerequisites
- Linux server with `syslog-ng` installed and running.
- Python 3.x installed on the server.
- `cron` for scheduling the script.

## Syslog-ng Configuration
1. Edit the `syslog-ng` configuration file (`/etc/syslog-ng/syslog-ng.conf`) to add the following configuration:
    ```conf
    source s_remote_udp {
        udp(ip(0.0.0.0) port(514));
    };

    destination d_aide {
        file("/var/log/remote/aide/$YEAR/$MONTH/$DAY/aidedata");
    };

    filter f_aide {
        program("aide");
    };

    log {
        source(s_remote_udp);
        filter(f_aide);
        destination(d_aide);
    };
    ```

2. Restart the syslog-ng service to apply the changes:
    ```sh
    sudo systemctl restart syslog-ng
    ```

## Scheduling the Script
1. Open the crontab configuration:

    ```sh
    crontab -e
    ```

2. Add the following line to schedule the script to run every day at midnight:
    ```sh
    0 0 * * * /usr/bin/python3 /path/to/scripts/aide_log_exporter.py
    ```

## Axonius Connector Configuration
Refer to the [Axonius CSV Adapter Documentation](https://docs.axonius.com/docs/csv) to configure the connector to import the generated CSV files. Ensure that the Axonius connector is set up to read from the directory where the CSV files are stored (`/path/to/csv`).

## Directory Structure
Ensure your directory structure looks something like this:
```plaintext
/var/log/remote/aide/     # AIDE logs collected by syslog-ng
/path/to/scripts/         # Directory containing the Python script
/path/to/csv/             # Directory where CSV files will be stored

