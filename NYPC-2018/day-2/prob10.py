from operator import itemgetter
stemina = int(input())
n = int(input())
contents = []
for i in range(n):
    u, e = input().split()
    contents.append((int(u), int(e), i+1))

def exp_choice(s):
    cont = sorted(contents, key=itemgetter(1), reverse=True)
    score = 0; num = 0; performed=[]
    for c in cont:
        if c[0] <= s:
            score += c[1]
            s -= c[0]
            num += 1
            performed.append(c[2])
    return score, num, performed

def ste_choice(s):
    cont = sorted(contents, key=itemgetter(0))
    score = 0; num = 0; performed=[]
    for c in cont:
        if c[0] <= s:
            score += c[1]
            s -= c[0]
            num += 1
            performed.append(c[2])
    return score, num, performed

dec1 = ste_choice(stemina)
dec2 = exp_choice(stemina)
result = dec1 if dec1[0] > dec2[0] else dec2
print(result[0])
print(result[1])
print(*result[2])
