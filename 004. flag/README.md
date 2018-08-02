# flag exploit

## py3
```
 ⚙ junhoyeo@Macbookui-MacBook-Pro  ~/Documents/pwnable.kr/4. flag   master ●  python3 exploit.py3
[*] '/Users/junhoyeo/Documents/pwnable.kr/4. flag/flag'
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE
    Packer:   Packed with UPX
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2017
UPX 3.94        Markus Oberhumer, Laszlo Molnar & John Reiser   May 12th 2017

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
    883745 <-    335288   37.94%   linux/amd64   flag

Unpacked 1 file.
[*] Unpacked ./flag
[*] '/Users/junhoyeo/Documents/pwnable.kr/4. flag/flag'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE
[*] function main at : 0x401164
[*]    0:   55                      push   ebp
       1:   48                      dec    eax
       2:   89 e5                   mov    ebp,esp
       4:   48                      dec    eax
       5:   83 ec 10                sub    esp,0x10
       8:   bf 58 66 49 00          mov    edi,0x496658
       d:   e8 0a 0f 00 00          call   0xf1c
      12:   bf 64 00 00 00          mov    edi,0x64
      17:   e8 50 88 00 00          call   0x886c
      1c:   48                      dec    eax
      1d:   89 45 f8                mov    DWORD PTR [ebp-0x8],eax
      20:   48                      dec    eax
      21:   8b 15 e5 0e 2c 00       mov    edx,DWORD PTR ds:0x2c0ee5
      27:   48                      dec    eax
      28:   8b 45 f8                mov    eax,DWORD PTR [ebp-0x8]
      2b:   48                      dec    eax
      2c:   89 d6                   mov    esi,edx
      2e:   48                      dec    eax
      2f:   89 c7                   mov    edi,eax
      31:   e8 86 f1 ff ff          call   0xfffff1bc
      36:   b8 00 00 00 00          mov    eax,0x0
      3b:   c9                      leave
[*] FLAG : UPX...? sounds like a delivery service :)
```

## ida64
```
 ⚙ junhoyeo@Macbookui-MacBook-Pro  ~/Documents/pwnable.kr/4. flag   master ●  upx -d ./flag
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2017
UPX 3.94        Markus Oberhumer, Laszlo Molnar & John Reiser   May 12th 2017

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
    883745 <-    335288   37.94%   linux/amd64   flag

Unpacked 1 file.
```
```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char *dest; // ST08_8

  puts("I will malloc() and strcpy the flag there. take it.", argv, envp);
  dest = (char *)malloc(100LL);
  strcpy(dest, flag);
  return 0;
}
```
```
.data:00000000006C2070                 public flag
.data:00000000006C2070 ; char *flag
.data:00000000006C2070 flag            dq offset aUpxSoundsLikeA
.data:00000000006C2070                                         ; DATA XREF: main+20↑r
.data:00000000006C2070                                         ; "UPX...? sounds like a delivery service "...
.data:00000000006C2078                 align 20h
```
```
.rodata:0000000000496628 aUpxSoundsLikeA db 'UPX...? sounds like a delivery service :)',0
.rodata:0000000000496628                                         ; DATA XREF: .data:flag↓o
.rodata:0000000000496652                 align 8
```
