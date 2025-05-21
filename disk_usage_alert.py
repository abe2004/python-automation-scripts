#!/usr/bin/env python3

import shutil
import smtplib

def check_disk_usage(disk, threshold):
    total, used, free = shutil.disk_usage(disk)
    percent_used = used / total * 100
    return percent_used > threshold

if check_disk_usage("/", 80):
    print("Warning: Disk space low.")

