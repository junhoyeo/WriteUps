n = int(input())
coord = []
for i in range(n):
    coord.append(tuple([int(number) for number in input().split()]))
x = [c[0] for c in coord]
y = [c[1] for c in coord]
print(sum(x)/n, sum(y)/n)
