# python3


def fib(number):
    a, b = 0, 1
    for i in range(number-1):
        print(i)
        a, b = b, a + b
    return b


def modulo(m):
    global sequence_list
    for i in range(2, fibb):
        print(i)
        sequence_list[i] = (sequence_list[i-1] + sequence_list[i-2]) % m
    return sequence_list

fibb, modul = [int(x) for x in input().split()]

sequence_list = [None] * fibb
sequence_list[0] = 0
sequence_list[1] = 1

print(modulo(modul))
# if fibb == 0:
#     print(0)
# else:
#     print((fib(fibb, modul)))



