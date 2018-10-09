# python3
import sys


def majority_element(a):
    temp = {}
    for i in range(0, len(a)):
        # print(i)
        if a[i] in temp:
            temp[a[i]] = temp.get(a[i], 0) + 1
        else:
            temp[a[i]] = 0
        # print(max(temp.values()))
    if max(temp.values())+1 > len(a) // 2:
        return 1
    else:
        return 0


input = sys.stdin.read()
data = list(map(int, input.split()))
n = data[0]
a = data[1:]
# print(len(a))
print(majority_element(a))