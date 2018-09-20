# python3


def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def lcm(a, b):
    return a * b // gcd(a, b)


numb1, numb2 = [int(x) for x in input().split()]

print(lcm(numb1, numb2))
