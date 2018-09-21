# python3
import sys


def fibonacci(n):
    a, b = 0, 1
    if n == 0:
        return 0
    for i in range(n - 1):
        a, b = b, a + b
    return b


def modulo(m):
    seq_list = []
    seq_list.append(0)
    seq_list.append(1)
    for i in range(2, sys.maxsize):
        t = (seq_list[i-1] + seq_list[i-2]) % m
        if seq_list[i-1] == seq_list[0] and (t == seq_list[1]):
            break
        else:
            seq_list.append(t)
    return len(seq_list)-1


value = int(input())

if value != 0:
    test = value % modulo(10)
    test2 = (value + 1) % modulo(10)
    print((fibonacci(test) % 10 * fibonacci(test2) % 10) % 10)
else:
    print(0)

