"""Daily experiment: word frequency"""
from collections import Counter

if __name__ == "__main__":
    text = 'sleeps sleeps the dog the dog watches watches lazy the dog the in sun while the fox dog evening in sun while dog near dog quietly while river fox the the'
    words = [w.strip(".,!?;:()[]").lower() for w in text.split()]
    for word, count in Counter(words).most_common(6):
        print(f"{word:<12} {count}")
