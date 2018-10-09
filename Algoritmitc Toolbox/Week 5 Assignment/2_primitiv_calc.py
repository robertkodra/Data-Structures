# python3
import sys

def primitive_calculator(number):
    numOperations = []
    # numOperations.append(number)
    while number > 1:
        if number == 10:
            number -= 1
            numOperations.append(number)
        elif number % 3 == 0:
            number //= 3
            numOperations.append(number)
        elif number % 2 == 0:
            number //= 2
            numOperations.append(number)
        else:
            number -= 1
            numOperations.append(number)
    # return len(numOperations)
    return numOperations


input = sys.stdin.read()
data = list(map(int, input.split()))
n = data[0]
print(primitive_calculator(n))
# https://www.coursera.org/learn/algorithmic-toolbox/discussions/weeks/5/threads/d8xwlPCNEeWkUAr_DMJ5Lw