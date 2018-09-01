def cluster(x, y):
    # https://stackoverflow.com/questions/18959255/flood-it-game-algorithm#answer-32034776
    # setup return value
    retval = set([])
    # stack
    col = grid[x][y]
    stk = []
    stk.append((x,y))
    while len(stk) > 0:
        curr = stk.pop()
        retval.add(curr)
        c_x = curr[0]
        c_y = curr[1]
        nbs = [(c_x,c_y+1),(c_x,c_y-1),(c_x+1,c_y),(c_x-1,c_y)]
        for i in nbs:
            if i[0] < n and i[0] >=0 and i[1] < n and i[1] >= 0:
                if grid[i[0]][i[1]] == col and not (i in retval):
                    stk.append(i)   
    return list(retval)

n, k = [int(i) for i in input().split()]
grid = []
if k != 0:
    colors = [int(i) for i in input().split()]
for i in range(n):
    grid.append([int(j) for j in input().split()])
for i in range(k):
    points = cluster(0, 0)
    for y, x in points:
        grid[y][x] = colors[i]
# print('=====')
# [print(*grid[i]) for i in range(n)]
points = cluster(0, 0)
# print(*points)
print(len(points))
