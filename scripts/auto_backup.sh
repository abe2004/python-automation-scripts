#!/bin/bash

# Directory to back up
SOURCE="/etc"

# Destination directory
DEST="/home/yourusername/backups"

# Create destination directory if it doesn't exist
mkdir -p "$DEST"

# Create backup with timestamp
DATE=$(date +%Y-%m-%d_%H-%M-%S)
BACKUP_FILE="$DEST/etc_backup_$DATE.tar.gz"

tar -czf "$BACKUP_FILE" "$SOURCE"

echo "Backup completed: $BACKUP_FILE"

