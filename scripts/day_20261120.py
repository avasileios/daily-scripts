"""Daily experiment: bubble sort trace"""
def bubble_sort(data):
    a = data[:]
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

if __name__ == "__main__":
    data = [61, 146, 121, 32, 8, -32, -24, 186, 41, 97]
    print("input :", data)
    print("sorted:", bubble_sort(data))
