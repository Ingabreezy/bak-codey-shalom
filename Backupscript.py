#!/usr/bin/env python3

import sys
import os
import subprocess
from datetime import datetime

def main():
    if len(sys.argv) != 3:
        print("Usage: bak_rsync.py <container_name> <volume_name>")
        sys.exit(1)

    container = sys.argv[1]
    volume = sys.argv[2]
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_dir = f"/backup/{volume}_{timestamp}"

    # Create the backup directory
    os.makedirs(backup_dir, exist_ok=True)

    # Construct the docker command
    docker_cmd = [
        "docker", "run", "--rm",
        "-v", f"{volume}:/data",
        "-v", f"{backup_dir}:/backup",
        "alpine",
        "sh", "-c", "cd /data && tar czf /backup/backup.tar.gz ."
    ]

    try:
        # Run the docker command
        subprocess.run(docker_cmd, check=True)
        print(f"Backup for {volume} completed at {backup_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error during backup: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
