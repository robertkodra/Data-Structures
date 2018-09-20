# python3


# def max_fast(list_numbers):
#     index1 = 1
#     for i in range(2, n):
#         if list_numbers[i] > list_numbers[index1]:
#             index1 = i
#
#     if index1 == 1:
#         index2 = 2
#     else:
#         index2 = 1
#
#     for i in range(2, n):
#         if list_numbers[i] != list_numbers[index1] and list_numbers[i] > list_numbers[index2]:
#             index2 = i
#     return list_numbers[index1] * list_numbers[index2]


def max_fast(list_numbers):
    return max(list_numbers)


n = int(input())
a = [int(x) for x in input().split()]

print(max_fast(a))
# product = 0

# for i in range(n):
#     for j in range(i+1, n):
#         product = max(product, a[i] * a[j])
#
# print(product)


