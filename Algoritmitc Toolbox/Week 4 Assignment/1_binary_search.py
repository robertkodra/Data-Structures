# python3
import sys


def binary_search(a, low, high, key):
    if high < low:
        return -1
    mid = low + (high-low)//2

    if key == a[mid]:
        return a.index(a[mid])
    elif key < a[mid]:
        return binary_search(a, low, mid - 1, key)
    else:
        return binary_search(a, mid + 1, high, key)


if __name__ == '__main__':
    inputS = sys.stdin.read()
    data = list(map(int, inputS.split()))
    n = data[0]
    m = data[n+1]
    a = data[1:n+1]
    for x in data[n+2:]:
        print(binary_search(a, 0, n - 1, x), end=" ")
