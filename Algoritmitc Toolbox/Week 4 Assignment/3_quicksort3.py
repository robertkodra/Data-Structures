# python3
import sys


def sort(a):
    less = []
    equal = []
    greater = []

    if len(a) > 1:
        pivot = a[0]
        for x in a:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)# Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array,
           # just return the array.
        return a


input = sys.stdin.read()
data = list(map(int, input.split()))
n = data[0]
a = data[1:]
print(*sort(a), sep=' ')
