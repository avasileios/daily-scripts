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
    data = [50, 111, -39, 77, 199, 99, 99, 142, 82]
    print("input :", data)
    print("sorted:", bubble_sort(data))
