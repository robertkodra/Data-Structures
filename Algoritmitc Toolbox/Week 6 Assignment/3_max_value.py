# Uses python3
import sys
import numpy as np
import operator
import re

def minmax(i,j):
    global matrix_max, matrix_min, operations
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    minimum = sys.maxsize
    maximum = -sys.maxsize
    # print(matrix_min[1][1])
    for k in range(i, j):
        # print(operations[k],matrix_max[i][k],matrix_max[k+1][j])
        # print(i, k, j)
        a = ops[operations[k]](matrix_max[i][k], matrix_max[k+1][j])
        b = ops[operations[k]](matrix_max[i][k], matrix_min[k+1][j])
        c = ops[operations[k]](matrix_min[i][k], matrix_max[k+1][j])
        d = ops[operations[k]](matrix_min[i][k], matrix_min[k+1][j])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
        # print(a,b,c,d)
    # print(minimum, maximum)
    return minimum, maximum


def get_maximum_value(dataset):
    global matrix_max, matrix_min, n
    for i in range(0, n):
        matrix_min[i][i] = dataset[i]
        matrix_max[i][i] = dataset[i]
    # print(n)
    # print(matrix_min)
    # print(matrix_max)
    for s in range(1, n):
        # print('the s is {}'.format(s))
        for i in range(0, n - s):
            j = i+s
            # print('the result for a{}{}'.format(i,j))
            matrix_min[i][j], matrix_max[i][j] = minmax(i, j)
    print(matrix_min)
    print(matrix_max)
    return int(matrix_max[0][n-1])


if __name__ == "__main__":
    data = input()
    data = re.findall('[+-/*]|\d+', data)
    operations = []
    dataset = []
    for x in data:
        if x == '+' or x == '*' or x == '/' or x == '-':
            operations.append(x)
        else:
            dataset.append(x)
    n = len(dataset)
    matrix_min = np.zeros((n, n))
    matrix_max = np.zeros((n, n))
    print(get_maximum_value(dataset))
    # print(len(dataset))