n = [int(number) for number in input().split()][0]
ans = 0
for i in range(n):
    line = input().split()
    for word in line:
        if word == 'NEXON':
            ans += 1
print(ans)
# 7, 19, 43, 698, 1831
