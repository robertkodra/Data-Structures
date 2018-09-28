# python3
denominations = [5, 1, 10]
denominations = sorted(denominations, reverse=True)

m = int(input())
temp = m
new_list = []

for obj in denominations:
    letter = temp // obj
    temp = temp % obj
    new_list += letter * [obj]


# myString = '+'.join(new_list)

# print("{}={}".format(m, '+'.join(map(str, new_list))))
print(len(new_list))
