"""Daily experiment: word frequency"""
from collections import Counter

if __name__ == "__main__":
    text = 'fox river the fox dog evening lazy brown the dog over evening sleeps the while the evening near evening brown quietly evening while dog the the in while lazy evening the evening dog the dog fox over evening lazy watches while'
    words = [w.strip(".,!?;:()[]").lower() for w in text.split()]
    for word, count in Counter(words).most_common(3):
        print(f"{word:<12} {count}")
