# python3


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    position = []
    j = 0
    for i, next in enumerate(text):
        # print("the i is {} and next is {}".format(i,next))

        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            position.append(i+1)
        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i+1
            if are_matching(opening_brackets_stack[-1], next):
                opening_brackets_stack.pop(-1)
                position.pop(-1)
            else:
                return i+1
    if opening_brackets_stack:
        return position[-1]
    return "Success"


if __name__ == "__main__":
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)
