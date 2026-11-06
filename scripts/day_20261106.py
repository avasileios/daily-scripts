"""Daily experiment: word frequency"""
from collections import Counter

if __name__ == "__main__":
    text = 'dog dog over fox fox watches evening watches watches the watches the jumps and the quietly sun the the sleeps watches river the quick while and the dog over evening river sun dog over the jumps'
    words = [w.strip(".,!?;:()[]").lower() for w in text.split()]
    for word, count in Counter(words).most_common(6):
        print(f"{word:<12} {count}")
