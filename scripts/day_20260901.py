"""Daily experiment: word frequency"""
from collections import Counter

if __name__ == "__main__":
    text = 'the over jumps quietly near and the watches while dog dog the over dog watches sun near quietly dog the the the fox sun jumps near watches the and the dog the sleeps brown and fox the river evening quick sleeps jumps sun sun the river brown over sleeps the the'
    words = [w.strip(".,!?;:()[]").lower() for w in text.split()]
    for word, count in Counter(words).most_common(4):
        print(f"{word:<12} {count}")
