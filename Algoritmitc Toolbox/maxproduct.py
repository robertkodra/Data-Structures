# python 3
n = int(input())
a = [int(x) for x in input().split()]

sort_list = sorted(a)
print(sort_list[n-1] * sort_list[n-2])