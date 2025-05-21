#!/usr/bin/env python3

import psutil
import time

with open("cpu_usage.log", "a") as log_file:
    for _ in range(12):  # Run for 1 minute, logs every 5 seconds
        usage = psutil.cpu_percent(interval=5)
        log_file.write(f"CPU Usage: {usage}%\n")
        print(f"Logged CPU usage: {usage}%")

