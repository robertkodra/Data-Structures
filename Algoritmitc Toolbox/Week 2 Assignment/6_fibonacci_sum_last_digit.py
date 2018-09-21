# python3
import sys


def fib(number):
    a, b = 0, 1
    for i in range(number-1):
        a, b = b, a + b
    return b


fibb = int(input())
modul = 10
sequence_list = []
sequence_list.append(0)
sequence_list.append(1)

for i in range(2, sys.maxsize):
    if sequence_list[i-1] == sequence_list[0] and (sequence_list[i-1] + sequence_list[i-2]) % modul == sequence_list[1]:
        break
    else:
        sequence_list.append((sequence_list[i-1] + sequence_list[i-2]) % modul)


# print(sequence_list)
# print(len(sequence_list)-1)
var1 = fibb % (len(sequence_list)-1)
# print(var1)
if var1 == 0:
    print(0)
else:
    print((fib(var1 + 2) - 1) % modul)




