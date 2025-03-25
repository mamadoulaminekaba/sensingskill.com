# 🔄 Restore Guide

## Manual Restore
Run this from your home directory:
./restore.sh

✅ This restores the latest backup into:
~/Desktop/restored_repo/

## Restore Specific Backup (Optional):
rsync -av /path/to/backup/ ~/Desktop/restored_repo/
