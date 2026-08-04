#!/bin/bash
# Daily push for avasileios/daily-scripts
# Runs the generator, commits any new log, pushes. Silent on success (no changes).
cd /var/www/projects/daily-scripts || exit 1

python3 generate_daily.py || exit 1

if [ -z "$(sudo git status --porcelain)" ]; then
  exit 0  # nothing new (already logged today)
fi

TODAY=$(date +%F)
sudo git add -A
sudo git -c user.name="Vasileios Antonopoulos" -c user.email="antvasileios@gmail.com" \
  commit -m "Daily log and scripts update ($TODAY)" > /dev/null 2>&1
sudo git push origin main > /dev/null 2>&1 || exit 1
exit 0
