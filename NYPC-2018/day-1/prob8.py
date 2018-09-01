import sys
sys.setrecursionlimit(999999999)

x, y = input().split()
x = int(x)
y = int(y)

def btn(a, b):
    return a + b

def rec(a, b):
    if a > x or b > y: return
    if (a, b) == (x, y):
        print('POSSIBLE')
        exit()
    rec(btn(a, b), b)
    rec(a, btn(a, b))

rec(1, 1)
if (x, y) == (1, 0):
    print('POSSIBLE')
    exit()
print('IMPOSSIBLE')

# 이거 했는데 시간초과? 였나 나서 C로 짜서 제출해서 50점 맞은 것 같은데 C 소스 실수로 날려먹음
