# collision exploit

## py3
```
 ⚙ junhoyeo@Macbookui-MacBook-Pro  ~/Documents/pwnable.kr/2. collision   master  python3 exploit.py3
[+] Connecting to pwnable.kr on port 2222: Done
[+] Downloading './col.c' to 'col.c': Found b'/home/col/col.c' in ssh cache
[*] hashcode : 568134124
[+] Opening new channel: './col `python -c \'print "\\xc8\\xce\\xc5\\x06"*4 + "\\xcc\\xce\\xc5\\x06"\'`': Done
[+] Recieving all data: Done (52B)
[*] Closed SSH channel with pwnable.kr
daddy! I just managed to create a hash collision :)

[*] FLAG : daddy! I just managed to create a hash collision :)
```

## py2
```
 ⚙ junhoyeo@Macbookui-MacBook-Pro  ~/Documents/pwnable.kr/2. collision   master ●  python2 exploit.py2
[+] Connecting to pwnable.kr on port 2222: Done
[!] Couldn't check security settings on 'pwnable.kr'
[+] Downloading './col.c' to 'col.c': Found '/home/col/col.c' in ssh cache
[*] hashcode : 568134124
[+] Opening new channel: './col \xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xc8\xce\xc5\x06\xcc\xce\xc5\x06': Done
[+] Receiving all data: Done (52B)
[*] Closed SSH channel with pwnable.kr
daddy! I just managed to create a hash collision :)

[*] FLAG : daddy! I just managed to create a hash collision :)
```
