#!/usr/bin/env python3
"""Generate today's daily log entry.

Creates logs/YYYY-MM-DD.md with a small, varied, human-looking daily entry:
date facts, a computation, a random Python tip and a quote.
Skips silently if today's file already exists (one commit per day).
"""
import datetime
import os
import random
import socket
import sys

PY_TIPS = [
    "Use `functools.lru_cache` to memoize expensive pure functions in one line.",
    "`defaultdict(list)` is perfect for grouping items by key.",
    "Named tuples from `collections` give readable, lightweight data objects.",
    "`zip(*matrix)` transposes a matrix — handy and fast.",
    "Prefer `pathlib.Path` over string path manipulation.",
    "`itertools.product` replaces nested loops cleanly.",
    "`str.format_map` with a dict is great for templates.",
    "Use `bisect` on sorted lists instead of linear scans.",
    "`heapq` gives you a priority queue without extra dependencies.",
    "`Counter.most_common(n)` finds top-n elements in one call.",
    "`enumerate(iterable, start=1)` fixes off-by-one index bugs.",
    "Type hints + `mypy` catch a surprising number of real bugs.",
    "`yield from` flattens nested generator delegation.",
    "`timeit` beats guessing when comparing two code snippets.",
    "A `dict` with `setdefault` acts like a mini autovivification.",
    "`re.DEBUG` shows how your regex actually compiles.",
    "`contextlib.suppress` replaces try/except pass for expected errors.",
    "`os.walk` + `pathlib` is all you need for file-tree jobs.",
    "`@dataclass` removes boilerplate from small value objects.",
    "Profiling with `cProfile` — profile first, optimize second.",
]

QUOTES = [
    "Simplicity is the soul of efficiency. — Austin Freeman",
    "First, solve the problem. Then, write the code. — John Johnson",
    "Any fool can write code that a computer can understand. — Martin Fowler",
    "Talk is cheap. Show me the code. — Linus Torvalds",
    "Programs must be written for people to read. — Harold Abelson",
    "The best way to predict the future is to invent it. — Alan Kay",
    "Simplicity is prerequisite for reliability. — Edsger Dijkstra",
    "Code is like humor. When you have to explain it, it's bad.",
    "Make it work, make it right, make it fast. — Kent Beck",
    "Premature optimization is the root of all evil. — Donald Knuth",
]


def primes_up_to(n: int) -> list:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, p in enumerate(sieve) if p]


def main() -> int:
    today = datetime.date.today()
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    os.makedirs(log_dir, exist_ok=True)
    target = os.path.join(log_dir, f"{today.isoformat()}.md")
    if os.path.exists(target):
        return 0  # already logged today — nothing to do

    day_of_year = today.timetuple().tm_yday
    n = random.randint(80, 300)
    primes = primes_up_to(n)
    tip = random.choice(PY_TIPS)
    quote = random.choice(QUOTES)
    year_progress = round(day_of_year / (366 if today.isocalendar()[1] > 52 else 365) * 100, 1)

    content = f"""# Daily Log — {today.strftime('%A, %d %B %Y')}

## Date facts
- Day of year: **{day_of_year}** ({year_progress}% through the year)
- Unix epoch: **{int(today.strftime('%s'))}**
- Week number: **{today.isocalendar()[1]}**

## Today's computation
Primes up to **{n}**: `{', '.join(map(str, primes))}`
- Count: **{len(primes)}**
- Largest prime: **{primes[-1]}**

## Python tip of the day
> {tip}

## Thought of the day
> {quote}

---
*Generated on {socket.gethostname()} · Python {sys.version.split()[0]} · {today.isoformat()}*
"""
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
