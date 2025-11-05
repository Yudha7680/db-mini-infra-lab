$telegramToken = "8089548485:AAGyCpXjsGrvpGaqPOMm5YHLhCogJq8S_uI"
$chatId = "1185024939"

function Send-TG {
    param([string]$msg)
    $url = "https://api.telegram.org/bot$telegramToken/sendMessage"
    Invoke-WebRequest -Uri $url -Method POST -ContentType "application/json" -Body (@{
        chat_id = $chatId
        text = $msg
    } | ConvertTo-Json) | Out-Null
}



$backupDir = "C:\db-mini-infra-lab\backups"
$logFile = "C:\db-mini-infra-lab\backup.log"
$date = Get-Date -Format "yyyyMMdd_HHmmss"
$backupFile = "$backupDir\backup_$date.sql"

# Run MySQL Dump
& "C:\xampp\mysql\bin\mysqldump.exe" -u root monitoring_lab > $backupFile

# Logging & Output
if (Test-Path $backupFile) {
    "$date - SUCCESS - Backup created: $backupFile" | Out-File -FilePath $logFile -Append
    Send-TG "✅ Backup SUCCESS: $backupFile"
    Write-Output "✅ Backup success: $backupFile"
} else {
    "$date - FAILED - Backup not created" | Out-File -FilePath $logFile -Append
    Send-TG "❌ Backup FAILED!"
    Write-Output "❌ Backup FAILED"
}


# Auto delete > 7 days
Get-ChildItem $backupDir -Filter "*.sql" | Where-Object {
    $_.LastWriteTime -lt (Get-Date).AddDays(-7)
} | Remove-Item
