# 제 2회 로그콘 - 프라푸치노좋아근데비싸. (4st, 9500)
옆동네 해킹방어과 예정

## Hello, LogCon!
> TeamLog{답}

`TeamLog{H3LL0_L0GC0N!}`

## 쾅!
> 네트워크에 결합하는 스토리지이며, 연결만 되어 있으면 자동으로 데이터가 백업이 되는 저장장치

`TeamLog{NAS}`

## 달수가 잘못했네
> 가연이가 바꾼 IP주소: 10011101.11110000.00001111.00100011 

```py
'.'.join([str(eval('0b'+i)) for i in '10011101.11110000.00001111.00100011'.split('.')])
# 157.240.15.35 -> https://www.facebook.com/
```

IP주소가 이진수로 되어 있는데 정수로 바꾸고 이를 이용해서 도메인을 구하면 된다.

`TeamLog{facebook.com}`

## 마인크래프트 업그레이드!
> 마크업 언어를 만드는데 사용하도록 권장하는 다목적 마크업 언어로, SGML의 단순화된 부분집합인 언어

`TeamLog{XML}`

## お前もう残っている!
> 하이퍼링크를 통해 사이트 방문시 남는 흔적 -> 방문자가 어떤 경로로 사이트에 방문했는지를 알 수 있음

`TeamLog{referrer}`

## 네 다음 스티브 잡스~
> 세계 최초의 웹 서버로 사용된 컴퓨터의 이름

`TeamLog{NeXT}`

## 개발-병 엌ㅋㅋㅋ
> 멀티태스킹 운영체제에서 사용자가 제어하지 않고, 백그라운드에서 여러 작업을 수행하는 프로그램의 이름

`TeamLog{daemon}`

## 품번박사 상준이!
정확한 커맨드는 기억이 안 나는데 조건이 아래와 같으니까 

- Gzip과 tar를 동시에 사용
- 압축과정을 하나로 보여줄 것

`tar`에 `-z`, `-v` 옵션 등등 써서 풀었던 것 같다.

`TeamLog{SSNI-029}`

## 비밀편지
> 압축파일 속 사진에서 볼 수 있는 TCP의 안정적인 전송을 위한 과정이다. 이 과정의 이름이 폴더의 암호이다.

TCP의 three way handshake에 관한 문제다.

3wayhandshake

`TeamLog{T34ML0G_1S_L0V3}`

## Becky
https://en.wikipedia.org/wiki/Eric_A._Meyer

`TeamLog{rebeccapurple}`

## 이것은 아니다 실행파일이

```py
s = 'TdcnHja|D:m;`9}P!bMg|&Iu},nD/qxb'
flag = []
for i, c in enumerate(s):
    flag.append(i ^ ord(c))
print(''.join([chr(i) for i in flag]))
```

리눅스 ELF 파일인데 맥이라서 걍 뜯었다.

`TeamLog{L3g0l4s_1s_th3_be5t_3lf}`

## 우째푸노그래피
네트워크 주소는 125.209.192.0이고 주어진 파일에 binwalk 돌리면 나온다.

`TeamLog{I_like_stegano}`

## 스풉키풉킼
> 호스트의 IP주소를 랜 카드의 하드웨어 주소로 변경하는 프로토콜을 변조하여 공격하는 기법

`TeamLog{ARPSpoofing}`

## 이것도 너프해 보시지!
> 민종이가 추천한 운동의 이름

스포츠? 안 봐도 태보 같은 걸!

https://i.pinimg.com/originals/7c/11/Nerf_this!/e5/7c11e5c837e74c914f27d9aa77fc1d8e.png

이런 pinimg 링크가 있는데 라우팅 형식에 안 맞으므로 `Nerf_this!`를 빼주면 된다.

https://i.pinimg.com/originals/7c/11/e5/7c11e5c837e74c914f27d9aa77fc1d8e.png

하하! 그럼 그렇지!

`TeamLog{taebohae}`

## 와! 언더테일 아시는구나!
`backgroundcolor` -> `background-color`

`background-color` property에 대해서 아냐고 물어보는 문제다. 제대로 바꾸면 글자 몇 개가 사라지는데, 모으면 플래그가 된다.

`TeamLog{HAWAWA}`

## αQμα Σαη
`ρng` -> `png`

이미지 링크 확장자에 `p`랑 비슷한 러시아어가 있는데 빼주면 된다.

https://i.pinimg.com/originals/84/1c/12/841c123332ee14cb9f9488a51daa8856.png

`TeamLog{moolmanboom}`

## 로그아웃
`chmod g+rw /teamlog` 

그룹에 read, write 권한을 준다.

`TeamLog{BY3..BY3..S30N..B43..}`

## 비트에 몸을 맡겨라!
https://en.wikipedia.org/wiki/Datagram_Congestion_Control_Protocol

얘다.

`TeamLog{DCCP}`

## 메리 크리스마스
RIP에서는 Hop Count가 16을 넘어가면 안된다.

`TeamLog{RIP}`

## 워싱턴DC
> 서버가 요청을 접수했지만 아직 처리하지 않았을 경우 전송되는 HTTP 상태 코드

`TeamLog{202}`

## 야!한 빨간 사이트..!
HTTP로 날아온 오브젝트 꺼내서 보면 Twice_background.png에 써있다.

`TeamLog{s2cr2tw2bs1t2}`

## HONUX
```
[HONUX@hoyeoni /]# find -name *.flag
/honux/LogCon/catme.flag
[HONUX@hoyeoni /]# cat /honux/LogCon/catme.flag​
VGVhbUxvZ3tIMFkzME4xXzFTX0gwTlVYX000U1QzUn0=
```

find 명령어로 플래그를 찾고 base64로 디코딩하면 나온다.

`TeamLog{H0Y30N1_1S_H0NUX_M4ST3R}`

## 몸통박치기!
https://www.npmjs.com/package/body-parser

`TeamLog{body-parser}`

## IP파라다이스
https://nodejs.org/api/net.html#net_net_isipv6_input

`TeamLog{net.isIPv6}`

## 못난 개발자라 죄송합니다악!
EJS에 맞게 고쳐 주자.

`TeamLog{<h1><%=score%></h1>}`

## 오잉?
`kernel`로 압축을 풀면 바이너리였나 하는 제목의 텍스트 파일에 이상한 언더바랑 대시가 있다.

```py
''.join([chr(eval('0b' + i)) for i in '_-_-_-__ _--__-_- _--____- _--_--_- _-__--__ _--_---- _--__--- _----_-- _-____-_ __--___- _-__---_ __--_-__ _-_-__-_ _-_--__- _-_----- _-__-_-- __--___- _-___-__ _-___-__ __--___- _-__---_ _-___--- _-----_-'.replace('_','0').replace('-','1').split(' ')])
```

진짜 바이너리다.

`TeamLog{B1N4RY_K1DD1NG}`

## power of guessing

```py
s = 'Crvz[xplnxbHverHvzvm~ypHpbrddre66j'
for i in range(256):
    if ord(s[0]) ^ i == ord('T'):
        print(i) # 23
```

일정 key로 XOR된 문자열이 나오는데, 플래그의 앞글자가 `T`니까 먼저 이걸로 key를 알아낸다.

```py
flag = ''.join([chr(ord(c) ^ 23) for c in s])
print(flag)
```

key가 23이라는 것을 알아냈으니 XOR을 돌려준다.

`TeamLog{you_are_amazing_guesser!!}`

## ClassIsDivine
`logo.svg`에서 로고 부분을 주석처리하면 나왔던 걸로 기억한다.

`TeamLog{Raise_your_Flag}`

## QuarteR
`SDN`으로 압축을 풀면 훼손된 QR 코드가 나타난다. 

paintbrush로 finder pattern을 메우고, 중간에 있는 낙서 쪽을 약간 만져준 다음 qrazybox에 올리면 복구해준다.

![](./qr.png)

`TeamLog{H0w_d1d_y0u_do_th1S??_GR3$T_J0B^_^}`

## 보물찾기(번외)

- 오우! 이런곳에서 주석을 찾으셨군요?! 개발자도구좀 볼 줄 아는 놈인가?! 로그콘 페이지 곳곳에서는 개발자들의 다양한 비하힌드 스토리를 찾아보실 수 있습니다. 문제를 플다가 조금 지루해진다면 잠깐 보물찾기 하듯이 비하인드 스토리를 찾아보는건 어떨까요? (사실 이것도 부장님 몰래 만든겁니다ㅎ 걸리면 어떻게 될지 몰라요;;)
- 아쿠아맨 개꿀잼 아쿠아맨 붐은 온다
- 아니 제가 카레를 진짜 못 먹는데 부모님이 저만빼고 외식하러 가신대요. 스프커리 먹으러 간다고 하시면서 먹고싶으면 너도 오라고 하심 ㅎ 카레 싫어하는거 알면서
- 로그콘 콘솔버전일때 회원가입 업데이트된거 서버에 올려야하는데 갑자기 부모님께 시골 납치됐다면서 못올린다고 연락와서 난리났었음. 다행히 당일 새벽에 돌아와서 금방 올릴 수 있었어여ㅎ
- 크리스마스때 놀지도 못하고 개발이나 하고있네ㅠㅠ
- 개발하면서 달팬 옆에 있는 이름없는 파스타 갔는데 ㄹㅇ JMT였음 여러분들도 꼭 가세요.
- 하와와 여고생쟝 열심히 해서 일등한 것이에양 호에에엥. 호의가 계속되면 호에엥인것이에요 호에에에에에에에에에엥
- 치킨이 먹고 싶어요 치킨 주세요 
- ... (이하생략)
  
