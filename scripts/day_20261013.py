"""Daily experiment: word frequency"""
from collections import Counter

if __name__ == "__main__":
    text = 'the the the the over dog over the in in the lazy dog over quick dog sun the fox evening while over the brown watches fox while quick river the fox sleeps while the quick over quick over in watches quietly over fox the sleeps the over river watches sleeps evening evening lazy the the the sun quick'
    words = [w.strip(".,!?;:()[]").lower() for w in text.split()]
    for word, count in Counter(words).most_common(4):
        print(f"{word:<12} {count}")
