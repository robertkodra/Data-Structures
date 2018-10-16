# Uses python3
import sys


def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


def dynamic_weight(W, w):
    matrix = [[0 for x in range(W+1)] for y in range(len(w)+1)]
    # print(W, len(w))
    for i in range(0, len(w)+1):
        matrix[i][0] = 0
    for j in range(0, W+1):
        matrix[0][j] = 0

    for i in range(1, len(w)+1):
        for j in range(1, W+1):
            matrix[i][j] = matrix[i-1][j]
            if w[i-1] <= j:
                val = matrix[i-1][j-w[i-1]] + w[i-1]
                # print(val)
                if matrix[i][j] < val:
                    matrix[i][j] = val
    # return matrix
    return matrix[len(w)][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    # print(optimal_weight(W, w))
    print(dynamic_weight(W, w))
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row])
    #              for row in dynamic_weight(W, w)]))