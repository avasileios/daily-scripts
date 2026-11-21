"""Daily experiment: word frequency"""
from collections import Counter

if __name__ == "__main__":
    text = 'brown sun lazy evening fox quietly sun the the brown river sun evening sleeps fox near while in the evening and in the dog the fox the watches while dog the over near the the river the quietly jumps lazy lazy jumps while the while fox'
    words = [w.strip(".,!?;:()[]").lower() for w in text.split()]
    for word, count in Counter(words).most_common(5):
        print(f"{word:<12} {count}")
