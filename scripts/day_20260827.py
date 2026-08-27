"""Daily experiment: word frequency"""
from collections import Counter

if __name__ == "__main__":
    text = 'dog near the dog the sleeps the brown jumps dog in watches fox brown the fox evening evening fox quick the watches sleeps fox quick in lazy while dog in sleeps watches and the near'
    words = [w.strip(".,!?;:()[]").lower() for w in text.split()]
    for word, count in Counter(words).most_common(4):
        print(f"{word:<12} {count}")
