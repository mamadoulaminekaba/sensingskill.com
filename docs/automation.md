# ⏰ Automation Guide (Cron Jobs)

## Step 1: Edit Crontab
export EDITOR=nano
crontab -e

## Step 2: Add Scheduled Backups:
0 2 * * * /Users/your-username/backup.sh >> /Users/your-username/backup.log 2>&1
0 3 * * 0 /Users/your-username/backup.sh >> /Users/your-username/backup.log 2>&1

## Step 3: Verify Cron Jobs:
crontab -l

## Step 4: Monitor Backup Logs:
cat ~/backup.log
