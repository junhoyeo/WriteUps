t = int(input())
ans = []
for testcase in range(t):
    n, m = [int(i) for i in input().split()]
    if (n == 2) and (m == 2):
        folds = []
        for i in range(n):
            folds += [int(i) for i in input().split()]
        for i in range(n - 1): 
            folds += [int(i) for i in input().split()]
        if (folds.count(1) is 1) or (folds.count(0) is 1):
            ans.append(1)
        else: ans.append(0)
    else:
        ver_folds = [[int(i) for i in input().split()] for i in range(n)]
        hor_folds = [[int(i) for i in input().split()] for i in range(n - 1)]
        answer = 1
        # print(ver_folds, hor_folds)
        for i in range(n-1):
            tmp = hor_folds[i]
            # print('[*]', tmp)
            order = None
            for idx, j in enumerate(tmp):
                # print((idx, j))
                if idx == 0:
                    order = not j
                if j == order:
                    answer = 0
                    break
                # print(int(order), j)
                order = j
            else: continue
            break
        ans.append(answer)
print(*ans)
