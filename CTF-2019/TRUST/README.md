# TRUST CTF - 준호,학원끝났다.결국,떡락했다.(27st, 656)
너무 놀았어,,,

## MIC CHECK!
> Flag : TRUST{Welcome_CTF_Have_FUN!}

`TRUST{Welcome_CTF_Have_FUN!}`

## Easy Taebo
> TRUST CTF에서도 태.보.해.
>
> Author : st4nw(조정훈)

```py
from pwn import *
taebo = {
    'left_jab' : '@==(^0^)@',
    'left_mid_jab' : '@=(^0^)@',
    'mid_jab' : '@(^0^)@',
    'right_mid_jab' : '@(^0^)=@',
    'right_jab' : '@(^0^)==@',
    'left_hook' : '@(^0^)@==',
    'right_hook' : '==@(^0^)@',
    'left_speedball' : '@@@(^0^)',
    'right_speedball' : '(^0^)@@@',
    'left_kick' : '@||(^0^)==@',
    'mid_kick' : '@==(^||^)==@',
    'right_kick' : '@==(^0^)||@'
}
r = remote('server.trustctf.com', 44923)
print r.recvuntil('>>')
for i in range(100):
    controls = r.recvuntil('>>').strip('\n').split('\n')[-1:][0].replace(' >>','').split(' : ')[1].split(' + ')
    pay = ''
    for cont in controls:
        pay += taebo[cont] + ' '
    log.info(pay)
    r.sendline(pay)
    print r.recv()
print r.recv()
print r.recv()
```

나중에 희성이 롸업을 보고 알았는데 마지막에 `print r.recvuntil('}')`로 썼으면 더 이뻤을 것이다. 흑흑...

`TRUST{w0w_y0u_9o7_4_w0nd3rfu1_b0dy_lik3_m3}`

## IDENTITY_5
> 확장자는 identity_5.apk 입니다. .zip을 지워주세요.
>
> I recommend excute it!!! and input "trust", "TRUST", "flag"!!!! have a good luck :)
>
> Author : m0nday(이동준)

주어지는 APK 파일을 디컴파일하고 QR코드 드래곤볼을 하면 된다.

http://www.javadecompilers.com/apk

여기서 온라인으로 디컴파일할 수 있다.

`TRUST{Th1s_1s_fl@g_@ndr0id_@dd_Qrc0d3}`

형 참고로 저 초콜릿 받았어요.

## MESS
> completely mess.
>
> Author : Edward(이규형)

올리디버거로 동적분석하면

```
00835163   68 00A08300      PUSH Mess.0083A000                       ; ASCII "S3CRe7PA5sW0rD"
```

패스워드 입력하면 플래그를 얻는다.

`TRUST{bBRWt>UHD?5wQ}`

## RSA1
> RSA 암호문 : 1649729212658550722856763813613372
> 암호화에 사용된 소수 1 : 36465956589847261
> 암호화에 사용된 소수 2 : 46496464168468673
> 복호화 키 : 1275312736838027047985273062147003 
> 플래그 형식:TRUST{~복호화값~}
> 
> Author : 생선스프

```py
from textwrap import wrap
from gmpy2 import mpz

p =  36465956589847261
q =  46496464168468673
c =  1649729212658550722856763813613372
n = p*q

d = 1275312736838027047985273062147003 
m = pow(mpz(c), d, n)
print m
# 65838295874878759585488995896489

print ''.join([chr(int(i)) for i in wrap(str(m), 2)])
# ASR_W0NK_U0Y_Y@Y
```

복호화된 값 `m`은 금방 구했는데 `TRUST{65838295874878759585488995896489}` 이게 인증이 안되서 뭐지 했다가 hex->ascii로 시도해봤는데 디코딩이 안되길래 잘못 풀었겠구나 하고 접었다.

나중에 알았는데 그냥 앞에서 두 바이트씩 끊어서 아스키로 바꾸기만 하면 됐었다.

`TRUST{ASR_W0NK_U0Y_Y@Y}`

## RSA2
> RSA 암호문 : 13879401797921631708823198002
> 암호화에 사용된 두 소수의 곱 : 443961743055319980564015263729
> 암호화키 : 34873453193
> 플래그 형식 : TRUST{~복호화값~}
> 
> Author : 생선스프

```py
from textwrap import wrap
from gmpy2 import mpz

c = 13879401797921631708823198002
n = 443961743055319980564015263729

d = 34873453193
m = pow(mpz(c), d, n)
print m

print ''.join([chr(int(i)) for i in wrap(str(m), 2)])
# L`B^:41!=NMV:8
```

`n`은 두 소수 `p`, `q`의 곱임을 이용해서 풀면 되...겠지?

역시 `m`까지만 구했었다. 끝나고 RSA1 문제처럼 플래그를 구해보려고 하니 저런 게 나오는데 플래그인지는 모르겠다.
