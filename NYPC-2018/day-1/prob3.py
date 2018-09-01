price = [int(number) for number in input().split()]
potion = price[0]
mana = price[1]
count = [0, 0]
n = int(input()) # W
if potion > mana: high, low = potion, mana    
else: high, low = mana, potion
high_num = n // high
low_num = 0
n %= high
while high_num >= 0:
    if n % low is 0:
        low_num = n // low
        n %= low
        break
    high_num -= 1
    n += high
if potion > mana: print(high_num, low_num)
else: print(low_num, high_num)
