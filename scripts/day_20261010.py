"""Daily experiment: word frequency"""
from collections import Counter

if __name__ == "__main__":
    text = 'quietly dog the in lazy dog fox the fox dog in sleeps brown dog sun while the fox watches near the river lazy the quick jumps dog dog jumps in the quick dog near jumps the in jumps jumps watches the sleeps lazy river river and jumps sun the over the watches while quick river evening'
    words = [w.strip(".,!?;:()[]").lower() for w in text.split()]
    for word, count in Counter(words).most_common(4):
        print(f"{word:<12} {count}")
