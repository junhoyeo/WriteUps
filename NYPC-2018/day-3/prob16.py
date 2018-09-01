import sys

def Dist(a, b):
    return abs(a - b)

m, n, k = [int(i) for i in input().split()]
candidates = [int(i) for i in input().split()]
units = [int(i) for i in input().split()]
units = sorted(units)
score = sys.maxsize
for i in candidates:
    s = max(Dist(units[0], i), Dist(units[n-1], i))
    if s < score: score = s
print(score)
