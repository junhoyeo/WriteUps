n = int(input())
blocks = []
for i in range(n):
    blocks.append([int(j) if (j != '-1') else None for j in input().split()])
for i in range(n-1, 0, -1):
    for idx in range(len(blocks[i])-1):
        if blocks[i][idx] != None and blocks[i][idx+1] != None:
            if blocks[i-1][idx] == None:
                blocks[i-1][idx] = (blocks[i][idx] + blocks[i][idx+1])%100
for line in blocks:
    print(*line)
