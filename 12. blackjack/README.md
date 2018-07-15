# blackjack exploit

## vul
`Enter Bet`에서 자신이 가진 캐시보다 더 많은 양을 걸면, 거절하고 재입력받는데 이때 값을 검증하지 않아서 취약점이 발생한다.

## run
위와 같은 방법으로 1억 달러를 걸고 돈이 털리거나 이길 때까지 계속 `hit`을 하는 스크립트를 작성해서 이길 때까지 돌렸다.

[ ] `Bankrupt` 당해도 종료하지 않고, 이길 때까지 끈질기게 게임을 다시 시작하게 수정하기(심심할 때)

```
 ⚙ junhoyeo@Macbookui-MacBook-Pro  ~/Documents/pwnable.kr/12. blackjack   master ●  python2 exploit.py2
[+] Opening connection to pwnable.kr on port 9009: Done





              222                111
            222 222            11111
           222   222          11 111
                222              111
               222               111

CCCCC     SS            DD         HHHHH    C    C
C    C    SS           D  D       H     H   C   C
C    C    SS          D    D     H          C  C
CCCCC     SS          D DD D     H          C C
C    C    SS         D DDDD D    H          CC C
C     C   SS         D      D    H          C   C
C     C   SS        D        D    H     H   C    C
CCCCCC    SSSSSSS   D        D     HHHHH    C     C

                        21
     DDDDDDDD      HH         CCCCC    S    S
        DD        H  H       C     C   S   S
        DD       H    H     C          S  S
        DD       H HH H     C          S S
        DD      H HHHH H    C          SS S
        DD      H      H    C          S   S
     D  DD     H        H    C     S   S    C
      DDD      H        H     CCCCC    S     S

         222                     111

   222                      111
       222                       111
      222222222222222      111111111111111
      2222222222222222    11111111111111111


                 Are You Ready?
                ----------------
                      (Y/N)


Enter 1 to Begin the Greatest Game Ever Played.
Enter 2 to See a Complete Listing of Rules.
Enter 3 to Exit Game. (Not Recommended)
Choice:

Cash: $500
-------
|D    |
|  7  |
|    D|
-------

Your Total is 7

The Dealer Has a Total of 5

Enter Bet: $
[*] Tring to bet $600

You cannot bet more money than you have.

Enter Bet:
[*] Tring to bet $100000000


Would You Like to Hit or Stay?
[*] hit

Please Enter H to Hit or S to Stay.

-------
|D    |
|  7  |
|    D|
-------

Your Total is 14

The Dealer Has a Total of 10

Would You Like to Hit or Stay?
Please Enter H to Hit or S to Stay.

[*] hit
-------

|D    |
|  7  |
|    D|
-------

Your Total is 21

The Dealer Has a Total of 15
Unbelievable! You Win!

You have 1 Wins and 0 Losses. Awesome!

Would You Like To Play Again?
Please Enter Y for Yes or N for No

[*] Play Again
[*] FLAG : YaY_I_AM_A_MILLIONARE_LOL
[*] Closed connection to pwnable.kr port 9009
```

현재는 `Bankrupt` 당하면 아래 출력처럼 바로 종료된다.

```
Would You Like to Hit or Stay?
Please Enter H to Hit or S to Stay.

[*] hit
-------


You Are Bankrupt. Game Over
Would You Like To Play Again?
Please Enter Y for Yes or N for No

[*] Bankrupt
[*] Closed connection to pwnable.kr port 9009
```
