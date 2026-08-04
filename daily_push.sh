#!/bin/bash
# Daily push for avasileios/daily-scripts — runs entirely on the local Ubuntu server.
#   * only commits inside a natural window (08:00-23:00)
#   * ~25% chance to skip on any given run (so the commit time varies)
#   * random commit message from a pool
# Silent on skip/success; prints an error message only on failure.
cd /home/alfanitaf/daily-scripts || exit 1

HOUR=$(date +%-H)
if [ "$HOUR" -lt 8 ] || [ "$HOUR" -gt 23 ]; then
  exit 0  # outside natural hours
fi

if [ $((RANDOM % 100)) -lt 25 ]; then
  exit 0  # skip this run — next run may do it
fi

python3 generate_daily.py || exit 1

if [ -z "$(git status --porcelain)" ]; then
  exit 0  # nothing new today
fi

TODAY=$(date +%F)
MESSAGES=(
  "Daily log and scripts update ($TODAY)"
  "Add today's experiment ($TODAY)"
  "Daily notes + new script"
  "Fresh daily entry"
  "Update logs and scripts"
  "Add daily experiment ($TODAY)"
)
MSG=${MESSAGES[$((RANDOM % ${#MESSAGES[@]}))]}

git add -A
git -c user.name="Vasileios Antonopoulos" -c user.email="antvasileios@gmail.com" \
  commit -m "$MSG" > /dev/null 2>&1 || exit 1
git push origin main > /dev/null 2>&1 || exit 1
exit 0
