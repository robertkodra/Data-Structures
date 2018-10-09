# python 3
import sys

def money_change(money, coins):
    minNumberCoins = {}

    minNumberCoins[0] = 0

    for m in range(1, money + 1):
        minNumberCoins[m] = sys.maxsize
        for obj in coins:
            if m >= obj:
                numCoins = minNumberCoins[m-obj] + 1
                if numCoins < minNumberCoins[m]:
                    minNumberCoins[m] = numCoins
    return minNumberCoins[money]


input = sys.stdin.read()
data = list(map(int, input.split()))
n = data[0]
coins = [1, 3, 4]
print(money_change(n, coins))
