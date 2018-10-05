# python3
import sys

def largest_number(a):
    #write your code here
    res = ""
    while a:
        maxDigit = max(a)
        for digits in a:
            # print("test")
            if check_digit(digits, maxDigit):
                # print(maxDigit, digits)
                maxDigit = digits
            res += str(maxDigit)
            # print(maxDigit)
            # print(a)
            a.remove(maxDigit)
            if a:
                maxDigit = max(a)
            # print("{} is the list, {} is the max digit and {} is the digit".format(a, maxDigit, digits))
    return res


def check_digit(a, b):
    # print("this is {} b from".format(b))
    if a // 10 == 0 :
        while b > 9:
            b = b // 10
        if a >= b:
            return True
        else:
            return False
    else:
        if a >= b:
            return True


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    a = data[1:]
    a.sort()
    # print(a)
    print(largest_number(a))