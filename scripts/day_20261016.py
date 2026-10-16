"""Daily experiment: word frequency"""
from collections import Counter

if __name__ == "__main__":
    text = 'the while the brown the the near dog fox watches while brown river the the quick river while sleeps river the over the dog in evening quick the the near brown the quick'
    words = [w.strip(".,!?;:()[]").lower() for w in text.split()]
    for word, count in Counter(words).most_common(3):
        print(f"{word:<12} {count}")
