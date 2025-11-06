# 🧠 MySQL Auto Backup & Monitoring Dashboard

A mini IT infrastructure project designed for **database backup automation**, **status monitoring**, and **alert notification** — built using **Python (Flask)**, **PowerShell**, and **MySQL (XAMPP)**.

---

## 🚀 Features

✅ **Automatic MySQL Backup**
- Scheduled daily backup using Windows Task Scheduler  
- Auto log file creation and rotation

✅ **Monitoring Dashboard**
- Built with Flask web app  
- Displays backup logs (Success / Failed)

✅ **Telegram Alert Bot**
- Sends success/failure notifications directly to Telegram

✅ **Backup Validation**
- Includes restore test and log verification

✅ **Auto Cleanup**
- Deletes old backups (older than 7 days)

---

## 🧩 Tech Stack

| Component | Tools / Tech |
|------------|--------------|
| OS | Windows 10 |
| Database | MySQL (XAMPP) |
| Language | Python 3.14, PowerShell |
| Web Framework | Flask |
| Task Scheduler | Windows Task Scheduler |
| Notification | Telegram Bot API |
| Version Control | Git & GitHub |

---

## 🗂️ Folder Structure

db-mini-infra-lab/
├── backups/ # .sql backup files (auto-generated)
├── dashboard/
│ ├── app.py # Flask dashboard app
│ ├── templates/
│ │ └── index.html # Web UI for backup logs
├── scripts/
│ └── mysql_backup.ps1 # PowerShell backup script
├── backup.py # Python-based backup script
├── backup.log # Backup activity log
└── screenshots/ # Documentation images


---
# 🧠 MySQL Auto Backup & Monitoring Dashboard

A mini IT infrastructure project designed for **database backup automation**, **status monitoring**, and **alert notification** — built using **Python (Flask)**, **PowerShell**, and **MySQL (XAMPP)**.

---

## 🚀 Features

✅ **Automatic MySQL Backup**
- Scheduled daily backup using Windows Task Scheduler  
- Auto log file creation and rotation

✅ **Monitoring Dashboard**
- Built with Flask web app  
- Displays backup logs (Success / Failed)

✅ **Telegram Alert Bot**
- Sends success/failure notifications directly to Telegram

✅ **Backup Validation**
- Includes restore test and log verification

✅ **Auto Cleanup**
- Deletes old backups (older than 7 days)

---

## 🧩 Tech Stack

| Component | Tools / Tech |
|------------|--------------|
| OS | Windows 10 |
| Database | MySQL (XAMPP) |
| Language | Python 3.14, PowerShell |
| Web Framework | Flask |
| Task Scheduler | Windows Task Scheduler |
| Notification | Telegram Bot API |
| Version Control | Git & GitHub |

---

## 🗂️ Folder Structure

db-mini-infra-lab/
├── backups/ # .sql backup files (auto-generated)
├── dashboard/
│ ├── app.py # Flask dashboard app
│ ├── templates/
│ │ └── index.html # Web UI for backup logs
├── scripts/
│ └── mysql_backup.ps1 # PowerShell backup script
├── backup.py # Python-based backup script
├── backup.log # Backup activity log
└── screenshots/ # Documentation images

yaml
Salin kode

---

## 🧰 Setup Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Yudha7680/db-mini-infra-lab.git
cd db-mini-infra-lab
2️⃣ Configure MySQL
Make sure MySQL is running (XAMPP).
Default user: root (no password).

3️⃣ Run Manual Backup
bash
Salin kode
py backup.py
Expected output:

yaml
Salin kode
✅ Backup created: C:\db-mini-infra-lab\backups\backup_YYYYMMDD_HHMMSS.sql
4️⃣ Start Flask Dashboard
bash
Salin kode
cd dashboard
py app.py
Then open your browser at 👉 http://127.0.0.1:5000

5️⃣ Set Up Scheduled Backup
Open Task Scheduler

Create new task → Run daily → Action:

arduino
Salin kode
powershell -File "C:\db-mini-infra-lab\scripts\mysql_backup.ps1"
Enable “Run with highest privileges”

📸 Screenshots
Step	Preview
Backup Status	
Backup Success	
Telegram Alert	
Task Scheduler	
Restore Check	

🧠 Author
👤 Yudha Andika Purwara
📍 Kabupaten Tangerang, Indonesia
📧 yudha.napoleon@gmail.com
🔗 LinkedIn Profile
📦 GitHub Projects

💡 Project Type
Educational portfolio project for IT Infrastructure (Database / Server) role.
Demonstrates automation, scripting, and system monitoring integration.
## 🧰 Setup Guide

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Yudha7680/db-mini-infra-lab.git
cd db-mini-infra-lab
