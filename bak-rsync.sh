#!/usr/bin/bash

# --------------------------------------------------------
# File:    bak-rsync.sh
# Author:  Codey Funston [cfeng44@github.com]
# Brief:   Performs rsync backup of passed in Docker volume.
# Changelog:
#   09/04/2025 - Initial creation. Not finished, only POC.
# --------------------------------------------------------

# Backup version naming
VOLUME_NAME="$1"
DATE=$(date)

# Backup location
SOURCE_DIR="/var/lib/docker/volumes/$VOLUME_NAME/"
DEST_DIR="/infra/bak/volume-backups/"
DEST_NAME="$DEST_DIR/$VOLUME_NAME/$DATE"

# Logs
RYSNC_LOG="/var/log/infra/bak/rsync.log"

# Main execution. Sends stderr to same place as stdout
mkdir --parents "$DEST_DIR"
rsync "$SOURCE_DIR" "$DEST_DIR" >>  "$RSYNC_LOG" 2>&1
