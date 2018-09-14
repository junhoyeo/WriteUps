# hackerschool LOB(Lord Of BOF)

## Probs
- [ ] LEVEL1 (gate -> gremlin) :  simple bof
- [ ] LEVEL2 (gremlin -> cobolt) : small buffer
- [ ] LEVEL3 (cobolt -> goblin) : small buffer + stdin
- [ ] LEVEL4 (goblin -> orc) : egghunter
- [ ] LEVEL5 (orc -> wolfman) : egghunter + bufferhunter
- [ ] LEVEL6 (wolfman -> darkelf) : check length of argv[1] + egghunter + bufferhunter
- [ ] LEVEL7 (darkelf -> orge) : check argv[0]
- [ ] LEVEL8 (orge -> troll) : check argc
- [ ] LEVEL9 (troll -> vampire) : check 0xbfff
- [ ] LEVEL10 (vampire -> skeleton) : argv hunter
- [ ] LEVEL11 (skeleton -> golem) : stack destroyer
- [ ] LEVEL12 (golem -> darkknight) : sfp 
- [ ] LEVEL13 (darkknight -> bugbear) : RTL1
- [ ] LEVEL14 (bugbear -> giant) : RTL2, only execve
- [ ] LEVEL15 (giant -> assassin) : no stack, no RTL
- [ ] LEVEL16 (assassin -> zombie_assassin) : fake ebp
- [ ] LEVEL17 (zombie_assassin -> succubus) : function calls
- [ ] LEVEL18 (succubus -> nightmare) : plt
- [ ] LEVEL19 (nightmare -> xavis) : fgets + destroyers
- [ ] LEVEL20 (xavis -> death_knight) : remote BOF 

## 설치 및 설정 

## 1. Installation

[http://hackerschool.org/TheLordofBOF/TheLordOfTheBOF_redhat_bootable.zip](http://hackerschool.org/TheLordofBOF/TheLordOfTheBOF_redhat_bootable.zip)

위 링크에서 이미지를 다운받아 VM을 만들고 부팅

## 2. Set default shell to `bash2`
```
$ vi /etc/passwd
:%s/bash/bash2/
:wq
```
기본 쉘을 `bash2`로 설정

## 3. Login
id `root`, pw `hackerschoolbof`로 로그인

## 4. With pwntools

### Install telnet(mac)
```
$ brew tap theeternalsw0rd/telnet
$ brew install telnet
```

### Python 2.7.15
```py
from pwn import *
p = process(['telnet', '-l', 'gate', '172.16.151.133'])
# telnet -l gate 172.16.151.133
p.recvuntil('Password:')
p.sendline('gate')
print p.recvuntil('[gate@localhost gate]$')
# Last login: Fri Sep 14 19:13:14 from 172.16.151.1
# unknown terminal "xterm-256color"
# [gate@localhost gate]$
```

사실 pwntools로 하다가 암걸릴뻔해서 그냥 telnet으로 했다.
