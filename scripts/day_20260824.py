"""Daily experiment: caesar cipher"""
def caesar(text, shift):
    out = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            out.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            out.append(ch)
    return "".join(out)

if __name__ == "__main__":
    msg = "And"
    shift = 3
    enc = caesar(msg, shift)
    print(f"original: {msg}")
    print(f"shift {shift}: {enc}")
    print(f"back    : {caesar(enc, -shift)}")
