# python3


def sum_of_two_digits(first_number, second_number):
    return first_number + second_number


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))