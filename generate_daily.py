#!/usr/bin/env python3
"""Generate today's daily entry: a log + a small random script experiment.

Creates logs/YYYY-MM-DD.md and scripts/day_YYYYMMDD.py with varied content
(random Python tip, quote, computation, and one of several small experiments).
Skips silently if today's files already exist.
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

EXPERIMENTS = [
    # (title, source code template with {data} / {params} placeholders)
    (
        "bubble sort trace",
        """def bubble_sort(data):
    a = data[:]
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

if __name__ == "__main__":
    data = {data}
    print("input :", data)
    print("sorted:", bubble_sort(data))
""",
    ),
    (
        "memoized fibonacci",
        """from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    for n in range({lo}, {hi}):
        print(f"fib({{n}}) = {{fib(n)}}")
""",
    ),
    (
        "caesar cipher",
        """def caesar(text, shift):
    out = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            out.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            out.append(ch)
    return "".join(out)

if __name__ == "__main__":
    msg = "{msg}"
    shift = {shift}
    enc = caesar(msg, shift)
    print(f"original: {{msg}}")
    print(f"shift {{shift}}: {{enc}}")
    print(f"back    : {{caesar(enc, -shift)}}")
""",
    ),
    (
        "word frequency",
        """from collections import Counter

if __name__ == "__main__":
    text = {text!r}
    words = [w.strip(".,!?;:()[]").lower() for w in text.split()]
    for word, count in Counter(words).most_common({top}):
        print(f"{{word:<12}} {{count}}")
""",
    ),
    (
        "prime sieve",
        """def primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, ok in enumerate(sieve) if ok]

if __name__ == "__main__":
    ps = primes_up_to({n})
    print(f"count: {{len(ps)}} primes, largest: {{ps[-1]}}")
    print(ps)
""",
    ),
    (
        "roman numerals",
        """def to_roman(num):
    vals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = []
    for v, s in vals:
        while num >= v:
            out.append(s)
            num -= v
    return "".join(out)

if __name__ == "__main__":
    for n in [{nums}]:
        print(f"{{n}} = {{to_roman(n)}}")
""",
    ),
]

WORDS = ("the quick brown fox jumps over the lazy dog and the dog sleeps "
         "while the fox watches quietly in the evening sun near the river").split()


def primes_up_to(n: int) -> list:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, p in enumerate(sieve) if p]


def build_experiment() -> tuple:
    title, template = random.choice(EXPERIMENTS)
    data = [random.randint(-50, 200) for _ in range(random.randint(6, 12))]
    if "bubble sort" in title:
        src = template.format(data=data)
    elif "fibonacci" in title:
        hi = random.randint(20, 35)
        src = template.format(lo=max(0, hi - 8), hi=hi)
    elif "caesar" in title:
        src = template.format(msg=random.choice(WORDS).capitalize(), shift=random.randint(1, 25))
    elif "frequency" in title:
        text = " ".join(random.choices(WORDS, k=random.randint(30, 60)))
        src = template.format(text=text, top=random.randint(3, 6))
    elif "prime" in title:
        src = template.format(n=random.randint(100, 400))
    else:
        src = template.format(nums=", ".join(str(random.randint(1, 3999)) for _ in range(4)))
    return title, src


def main() -> int:
    today = datetime.date.today()
    base = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base, "logs")
    scr_dir = os.path.join(base, "scripts")
    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(scr_dir, exist_ok=True)

    stamp = today.strftime("%Y-%m-%d")
    log_path = os.path.join(log_dir, f"{stamp}.md")
    if os.path.exists(log_path):
        return 0  # already done today

    day_of_year = today.timetuple().tm_yday
    n = random.randint(80, 300)
    primes = primes_up_to(n)
    tip = random.choice(PY_TIPS)
    quote = random.choice(QUOTES)
    title, src = build_experiment()
    scr_name = f"day_{today.strftime('%Y%m%d')}.py"

    log_content = f"""# Daily Log — {today.strftime('%A, %d %B %Y')}

## Date facts
- Day of year: **{day_of_year}**
- Unix epoch: **{int(today.strftime('%s'))}**
- Week number: **{today.isocalendar()[1]}**

## Today's computation
Primes up to **{n}**: `{', '.join(map(str, primes))}` ({len(primes)} primes, largest {primes[-1]})

## Experiment of the day
Small script: [`scripts/{scr_name}`](scripts/{scr_name}) — *{title}*

## Python tip of the day
> {tip}

## Thought of the day
> {quote}

---
*Generated on {socket.gethostname()} · Python {sys.version.split()[0]} · {stamp}*
"""
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(log_content)
    with open(os.path.join(scr_dir, scr_name), "w", encoding="utf-8") as f:
        f.write(f'"""Daily experiment: {title}"""\n')
        f.write(src)
    return 0


if __name__ == "__main__":
    sys.exit(main())
