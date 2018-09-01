# from operator import itemgetter
# n, m = [int(i) for i in input().split()]
# infected = [1]
# events = [[int(i) for i in input().split()] for i in range(m)]
# events = sorted(events, key=itemgetter(2))
# for e in events:
#     inf_0 = e[0] in infected
#     inf_1 = e[1] in infected
#     if inf_0 and inf_1: continue
#     if inf_0 and not inf_1:
#         infected.append(e[1])
#     if inf_1 and not inf_0:
#         infected.append(e[0])
# print(*sorted(infected))
from operator import itemgetter
n, m = [int(i) for i in input().split()]
infected = set([1])
events = [[int(i) for i in input().split()] for i in range(m)]
events = sorted(events, key=itemgetter(2))
for p1, p2, t in events:
    if (p1 in infected) or (p2 in infected):
        infected.add(p1)
        infected.add(p2)
print(*sorted(infected))
