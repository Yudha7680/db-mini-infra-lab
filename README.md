# Automated MySQL Backup & Monitoring System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![MySQL](https://img.shields.io/badge/MySQL-Backup%20Automation-orange)
![PowerShell](https://img.shields.io/badge/PowerShell-Automation-blue)
![Windows](https://img.shields.io/badge/OS-Windows-green)
![Status](https://img.shields.io/badge/Project-Active-success)

> Lightweight infra project for automatic database backup, logging, restore validation, and notification via Telegram.

---

## Overview

This project simulates a **real-world IT Infrastructure / Database Support workflow**:

* ✅ Scheduled MySQL backup (Windows Task Scheduler)
* ✅ Backup rotation (auto delete older than 7 days)
* ✅ Backup verification log
* ✅ Restore test database
* ✅ Telegram alert (success / fail)
* ✅ Flask dashboard to monitor logs

Built to demonstrate **infra mindset + scripting + automation**.

---

## Tech Stack

| Layer         | Technology              |
| ------------- | ----------------------- |
| Database      | MySQL / MariaDB (XAMPP) |
| Automation    | PowerShell              |
| Backup Engine | mysqldump               |
| Monitoring    | Python + Flask          |
| Alerting      | Telegram Bot API        |
| OS            | Windows                 |
| Logging       | File log system         |

---

## Folder Structure

```
db-mini-infra-lab/
 ├─ backups/
 ├─ scripts/
 │   └─ mysql_backup.ps1
 ├─ dashboard/
 │   ├─ app.py
 │   └─ templates/
 │       └─ index.html
 ├─ backup.py
 └─ backup.log
```

---

## Manual Run Backup

```
cd C:\db-mini-infra-lab
py backup.py
```

Expected:

```
SUCCESS - Backup created
```

---

## Task Scheduler Command

```
powershell.exe -File "C:\db-mini-infra-lab\scripts\mysql_backup.ps1"
```

Trigger: **Daily @ 02:00 AM**

---

## Restore Test

```
DROP DATABASE IF EXISTS test_restore;
CREATE DATABASE test_restore;
mysql test_restore < backups/backup_xxx.sql;
SHOW TABLES;
```

Expected output: tables successfully loaded.

---

## System Flow Diagram

*(Insert image)*

---

## Key Features

* Backup automation
* Backup integrity check
* Database restore validation
* Log display via dashboard
* Realtime alert

---

## Sample Telegram Alert

```
✅ Backup SUCCESS
File: backup_2025...
Path: C:\db-mini-infra-lab\backups
```

---

## Results

| Feature        | Status |
| -------------- | ------ |
| Auto backup    | ✅      |
| Dashboard      | ✅      |
| Restore test   | ✅      |
| Retention      | ✅      |
| Telegram alert | ✅      |
| Manual run     | ✅      |

---

## Next Improvements

* Remote backup (SFTP / AWS S3)
* AES encryption
* Docker version
* Prometheus metrics

---

## Author

**Yudha Andika Purwara** — IT Infrastructure Enthusiast

---

> Evidence screenshots included below 👇 (will be filled after upload limit reset).
