"""Daily experiment: word frequency"""
from collections import Counter

if __name__ == "__main__":
    text = 'and near fox watches dog lazy sun dog the the and dog fox lazy quietly over watches sun the sleeps jumps jumps quietly fox lazy sleeps in sleeps the quietly while while jumps fox dog sleeps watches evening river while fox dog evening over over watches the while the quick evening the near sun lazy dog fox over'
    words = [w.strip(".,!?;:()[]").lower() for w in text.split()]
    for word, count in Counter(words).most_common(3):
        print(f"{word:<12} {count}")
