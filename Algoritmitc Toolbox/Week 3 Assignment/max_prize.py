# python3

def max_candies(candies):
    prizes = []
    i = 1
    statement = True
    while statement:
        # print('{} candies, {} i iteration'.format(candies, i))
        if candies - i > i and i * 2 +1 <= n:
            prizes.append(i)
            candies -= i
            i += 1
        else:
            statement = False
            prizes.append(candies)
    return prizes


n = int(input())
prizes = max_candies(n)

print(len(prizes))
print("{}".format(' '.join(map(str, prizes))))