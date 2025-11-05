import os
import datetime
import subprocess

# MySQL credentials
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
BACKUP_DIR = r"C:\db-mini-infra-lab\backups"
LOG_FILE = r"C:\db-mini-infra-lab\backup.log"

# Create backup folder if not exists
os.makedirs(BACKUP_DIR, exist_ok=True)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = os.path.join(BACKUP_DIR, f"backup_{timestamp}.sql")

try:
    cmd = [
    r"C:\xampp\mysql\bin\mysqldump.exe",
    f"-u{MYSQL_USER}",
    "monitoring_lab",
    "--single-transaction",
    "--skip-lock-tables",
    "--no-tablespaces",
    f"--result-file={backup_file}"
]


    subprocess.run(cmd, check=True)
    msg = f"{timestamp} - SUCCESS - Backup created: {backup_file}"

except Exception as e:
    msg = f"{timestamp} - FAILED - {str(e)}"

# Write log
with open(LOG_FILE, "a", encoding="utf-8") as log:
    log.write(msg + "\n")

print(msg)
