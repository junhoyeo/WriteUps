# 2nd 국민대X우분투 청소년 CTF WriteUp
## (MISC) Introduce
```
ubuntu{dlrpqkfhvmfform}
```
괄호 사이의 부분만 인증하면 된다.
## (MISC) OpenMe
```
ubuntu{3ncrypt3d_zip_fil3_i5_fun_t0_s0lv3}
```
본격 ZIP 파일 브포문제! 팀원당 하나씩 상위폴더 맡아서 하나씩 벗겨나갔다.
그때는 몰랐는데 Python으로 Script 짜서 풀면 굳이 그 고생을 안 해도 됬을 텐데...~~대신 우정을 얻었습니다~~
## (Web) Js Counter
```
ub?nu{Js_ls_s1mpl3!!!}
```
페이지 소스에 있는 난독화된 JavaScript 코드를 난독화 해제한 뒤, flag_back 배열의 값을 하나씩 ^11 연산시키면 플래그가 나온다.

Teamname : hyunjundaBang
With 김현준, 홍다오
