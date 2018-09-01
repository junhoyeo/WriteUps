# from pwn import *
# key = []
# ans = []
# for n in range(1, 11):
#     for k in range(n+1):
#         p = process(['python3', 'today1.py'])
#         p.sendline('{} {}'.format(str(n), str(k)))
#         key.append((n, k))
#         ans.append(int(p.recvline().strip()))
# print key
# print ans

from pwn import *
key = []
ans = []
for n in range(1, 501):
    k = n
    p = process(['python3', 'today1.py'])
    p.sendline('{} {}'.format(str(n), str(k)))
    key.append((n, k))
    ans.append(int(p.recvline().strip()))
print key
print ans
