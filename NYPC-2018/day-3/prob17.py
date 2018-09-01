from itertools import groupby
n = int(input())
blocks = input()
prev = None
combo = 0
while True:
    tmp = blocks
    chains = ["".join(grp) for num, grp in groupby(blocks)]
    blocks = ''.join([c for c in chains if len(c) < 3])
    if blocks == prev:
        print(combo)
        if blocks == '':
            print('PERFECT!!!')
        else: print(blocks)
        break
    prev = blocks
    if tmp != blocks:
        combo += 1
