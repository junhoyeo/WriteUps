## #1. [Password Recover... (xcz.kr-prob17)](http://xcz.kr/START/prob/prob17.php)
`IDISLIE`

## #2. [Network Recovery! (xcz.kr-prob13)](http://xcz.kr/START/prob/prob13.php)
pcapfix로 먼저 봤는데 문제가 없었다.

```
[*] Your pcap file looks proper. Nothing to fix!
```

`.pcapng` 확장자를 주니 와이어샤크로 열렸고, HTTP 통신으로 받은 오브젝트를 추출할 수 있었다.

```bash
$ ls
%2f         favicon.ico index.html  treasure1   treasure2   treasure3
$ file treasure1
treasure1: PNG image data, 700 x 350, 8-bit/color RGB, non-interlaced
$ file treasure2
treasure2: data
$ file treasure3
treasure3: data
$ cat treasure1 treasure2 treasure3 > treasure.png
```

![](./prob-2/treasure.png)

```py
>>> hashlib.md5('NET₩oRK1sFun'.encode('utf-8')).hexdigest()
'a7aa98416c3701ec5db2f31014cda375' # Wrong
>>> hashlib.md5('NET\oRK1sFun'.encode('utf-8')).hexdigest()
'2f4a11572d9ff67baebdb2f3899d7a84' # Correct
```
