n, a, b = [int(i) for i in input().split()]
record = input()
score = []
r = []
for i in range(int(n/2)):
    for j in range(int(n/2)):
        tmp = record[i:j]
        if tmp not in r:
            v1 = record.count(tmp)
            if v1 < 2: 
                continue
            rst = v1*len(tmp)
            r.append(tmp)
            score.append(rst)
# print(*r)
# print(score)
max = 0
for i in range(len(score)):
    if score[i] > score[max]:
        max = i
# routine = r[max]
score = score[max]
# print(score)
if score > b:
    print(1) # bot
elif score < a:
    print(3) # human
else:
    print(2) # human or bot
