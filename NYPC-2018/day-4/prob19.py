t = int(input())
ans = []
for testcase in range(t):
    n, m = [int(i) for i in input().split()]
    folds = []
    for i in range(n):
        folds += [int(i) for i in input().split()]
    for i in range(n-1): 
        folds += [int(i) for i in input().split()]
    if (folds.count(1) is 1) or (folds.count(0) is 1):
        ans.append(1)
    else: ans.append(0)
print(*ans)
