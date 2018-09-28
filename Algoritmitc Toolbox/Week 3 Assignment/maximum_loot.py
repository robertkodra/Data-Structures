# Uses python3
import sys


def get_optimal_value(backpack, w, v):
    value = 0.
    for i in range(n):
        if backpack == 0 and backpack >= 0:
            return value
        a = min(weights[i], backpack)
        print("{} is a and for capacity is {} ".format(a, backpack))
        value = value + a * (v[i]/w[i])
        w[i] = w[i] - a
        backpack = backpack - a
        print(backpack)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
