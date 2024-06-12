import os
import zipfile
from datetime import datetime

DB_FILE = 'identifier.sqlite'
LOG_FILE = 'logs.db'
BACKUP_DIR = 'backup'


def create_backup():
    backup_filename = os.path.join(BACKUP_DIR, f'backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.zip')
    with zipfile.ZipFile(backup_filename, 'w') as backup_zip:
        backup_zip.write(DB_FILE)
        backup_zip.write(LOG_FILE)
    print(f"Backup created: {backup_filename}")


def restore_backup(backup_filename):
    with zipfile.ZipFile(backup_filename, 'r') as backup_zip:
        backup_zip.extractall()
    print(f"Backup restored from: {backup_filename}")
