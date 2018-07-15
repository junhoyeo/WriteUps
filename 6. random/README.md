# random exploit
`ctypes` 써보려다가 실패해서 그냥 gdb에서 찾은 값 사용
```
random@ubuntu:~$ gdb -q ./random
Reading symbols from ./random...(no debugging symbols found)...done.
(gdb) disass main
Dump of assembler code for function main:
   0x00000000004005f4 <+0>:     push   %rbp
   0x00000000004005f5 <+1>:     mov    %rsp,%rbp
   0x00000000004005f8 <+4>:     sub    $0x10,%rsp
   0x00000000004005fc <+8>:     mov    $0x0,%eax
   0x0000000000400601 <+13>:    callq  0x400500 <rand@plt>
   0x0000000000400606 <+18>:    mov    %eax,-0x4(%rbp)
   0x0000000000400609 <+21>:    movl   $0x0,-0x8(%rbp)
   0x0000000000400610 <+28>:    mov    $0x400760,%eax
   0x0000000000400615 <+33>:    lea    -0x8(%rbp),%rdx
   0x0000000000400619 <+37>:    mov    %rdx,%rsi
   0x000000000040061c <+40>:    mov    %rax,%rdi
   0x000000000040061f <+43>:    mov    $0x0,%eax
---Type <return> to continue, or q <return> to quit---q
Quit
(gdb) b *main+18
Breakpoint 1 at 0x400606
(gdb) r
Starting program: /home/random/random

Breakpoint 1, 0x0000000000400606 in main ()
(gdb) info registers
rax            0x6b8b4567       1804289383
rbx            0x0      0
rcx            0x7f900b2e80a4   140256639615140
rdx            0x7f900b2e80a8   140256639615144
rsi            0x7ffd55d36b3c   140726043372348
rdi            0x7f900b2e8620   140256639616544
rbp            0x7ffd55d36b70   0x7ffd55d36b70
rsp            0x7ffd55d36b60   0x7ffd55d36b60
r8             0x7f900b2e80a4   140256639615140
r9             0x7f900b2e8120   140256639615264
r10            0x47f    1151
r11            0x7f900af5ff50   140256635912016
r12            0x400510 4195600
---Type <return> to continue, or q <return> to quit---
```

random is `0x6b8b4567`

```
 junhoyeo@Macbookui-MacBook-Pro  ~/Documents/pwnable.kr/6. random   master  python2 exploit.py2
[+] Connecting to pwnable.kr on port 2222: Done
[!] Couldn't check security settings on 'pwnable.kr'
[+] Downloading './random' to 'random': Found '/home/random/random' in ssh cache
[+] Downloading './random.c' to 'random.c': Found '/home/random/random.c' in ssh cache
[*] random : 1804289383
[*] key : 3039230856
[+] Opening new channel: './random': Done
Good!

[*] FLAG : Mommy, I thought libc random is unpredictable...
[*] Closed SSH channel with pwnable.kr
```
