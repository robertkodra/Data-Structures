# python3
import sys

def max_dot_product(x, y):
    # print()
    res = 0
    for i in range(len(x)):
        res += x[i] * y[i]
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)

    print(data)
    # print(max_dot_product(a, b))