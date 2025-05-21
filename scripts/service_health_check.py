#!/usr/bin/env python3

import subprocess

def check_service_status(service_name):
    result = subprocess.run(['systemctl', 'is-active', service_name], stdout=subprocess.PIPE)
    status = result.stdout.decode().strip()
    if status == "active":
        print(f"{service_name} is running ✅")
    else:
        print(f"{service_name} is NOT running ❌")

# Example usage:
services = ["ssh", "nginx", "cron"]
for service in services:
    check_service_status(service)

