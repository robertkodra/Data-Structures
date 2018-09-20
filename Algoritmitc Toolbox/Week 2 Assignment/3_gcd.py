# python3

a, b = [int(x) for x in input().split()]

while a % b != 0:
    a, b = b, a % b

print(b)
