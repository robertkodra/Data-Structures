# python3
import sys


def fib(number):
    a, b = 0, 1
    for i in range(number-1):
        a, b = b, a + b
    return b


fibb_start, fibb_end = [int(x) for x in input().split()]
modul = 10
sequence_list = []
sequence_list.append(0)
sequence_list.append(1)


for i in range(2, sys.maxsize):
    if sequence_list[i-1] == sequence_list[0] and (sequence_list[i-1] + sequence_list[i-2]) % modul == sequence_list[1]:
        break
    else:
        sequence_list.append((sequence_list[i-1] + sequence_list[i-2]) % modul)


if fibb_start == fibb_end:
    # print("Normal fibb")
    var1 = fibb_start % (len(sequence_list)-1)
    if var1 == 0:
        print(0)
    else:
        print((fib(var1)) % modul)

elif fibb_start < fibb_end:
    # print("2nd way")
    var1 = fibb_start % (len(sequence_list)-1)
    var2 = fibb_end % (len(sequence_list)-1)
    if var1 == 0 and var2 == 0:
        print(0)
    else:
        # print("Var1= {} and var2= {}".format(var1, var2))
        # print((fib(var2 + 2) - 1) % modul)
        # print((fib(var1 + 1) - 1) % modul)
        print(((fib(var2 + 2) - 1) - (fib(var1 + 1) - 1)) % modul)
