# #include <stdio.h>
# #include <string.h>
# int n;
# void floodFillUtil(int grid[][n], int x, int y, int prevC, int newC){
# // https://www.geeksforgeeks.org/flood-fill-algorithm-implement-fill-paint/
#     if (x < 0 || x >= n || y < 0 || y >= n)
#         return;
#     if (grid[x][y] != prevC)
#         return;
#     grid[x][y] = newC;
#     floodFillUtil(grid, x+1, y, prevC, newC);
#     floodFillUtil(grid, x-1, y, prevC, newC);
#     floodFillUtil(grid, x, y+1, prevC, newC);
#     floodFillUtil(grid, x, y-1, prevC, newC);
# }
# void floodFill(int grid[][n], int newC){
#     int prevC = grid[0][0];
#     floodFillUtil(grid, 0, 0, prevC, newC);
# }
# int main(){
#     int k;
#     scanf("%d %d", &n, &k);
#     int colors[k];
#     for (int i = 0; i < k; i++)
#         scanf("%d", &colors[i]);
#     int grid[n][n];
#     for (int i = 0; i < n; i++){
#         for (int j = 0; j < n; j++)
#             scanf("%d", &grid[i][j]);
#     }
#     for (int i = 0; i < k; i++)
#         floodFill(grid, colors[i]);
#     floodFill(grid, -1);
#     int count = 0;
#     for (int i = 0; i < n; i++){
#         for (int j = 0; j < n; j++)
#             if (grid[i][j] == -1) count++;
#     }
#     printf("%d\n", count);
#     return 0;
# }
from pwn import *
import random
p = process('./wow2.out')
n, k = [int(i) for i in input().split()]
if k != 0:
    colors = [str(random.randint(0, 9)) for j in range(k)]
p.sendline(str(n) + ' ' + str(k))
print(n, k)
p.sendline(' '.join(colors))
print(*colors)
grid = []
for i in range(n):
    grid.append([str(random.randint(0, 9)) for j in range(n)])
for line in grid:
    print(*line)
    p.sendline(' '.join(line))
print(p.recvline(timeout=1).decode().strip())
