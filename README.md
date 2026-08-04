# Daily Scripts

**A self-running daily automation repository** — a Python generator, a cron
wrapper, and a growing log of small experiments, one entry per day.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![Bash](https://img.shields.io/badge/Bash-automation-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#)

---

## How it works

A cron job on a home Ubuntu server runs `daily_push.sh` several times a day.
Within a natural window (08:00–23:00) it:

1. runs `generate_daily.py`, which creates two files for today:
   - `logs/YYYY-MM-DD.md` — date facts, a computation, a Python tip and a quote
   - `scripts/day_YYYYMMDD.py` — a small random experiment from a rotating pool
2. commits everything with a randomized message, and pushes.

Small deliberate randomness (a ~25% chance to skip a run, varied commit
times and messages) keeps the activity graph looking organic rather than
machine-stamped.

## Structure

| Path | Purpose |
| :--- | :--- |
| `generate_daily.py` | Creates the daily log + script entry (idempotent, skips if today exists) |
| `daily_push.sh` | Cron wrapper — window check, skip logic, commit + push |
| `logs/` | Markdown daily entries |
| `scripts/` | The small daily Python experiments |

## Why

- **Consistency** — a visible commit every single day for years.
- **Habit** — a low-friction way to write code daily without a big time cost.
- **Variety** — the generator cycles through different experiment types, so
  the repo keeps growing in different directions.

## Usage

```bash
python3 generate_daily.py          # create todays entry
git add -A && git commit -m "daily" # commit
git push                            # push
```

Or just wire `daily_push.sh` into cron:

```cron
*/45 8-23 * * * /path/to/daily-scripts/daily_push.sh
```

## License

[MIT](./LICENSE) © 2026 Vasileios Antonopoulos
