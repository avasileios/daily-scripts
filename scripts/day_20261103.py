"""Daily experiment: word frequency"""
from collections import Counter

if __name__ == "__main__":
    text = 'watches sun over the the the brown the the watches the quick the dog near over the in the evening jumps jumps fox in lazy sun sleeps and watches in the fox the dog sun the river quick jumps'
    words = [w.strip(".,!?;:()[]").lower() for w in text.split()]
    for word, count in Counter(words).most_common(4):
        print(f"{word:<12} {count}")
