# python3


def fib(number):
    a, b = 0, 1
    for i in range(number-1):
        a, b = b, a + b
    return b


n = int(input())

if n == 0:
    print(0)
else:
    print((fib(n)))
