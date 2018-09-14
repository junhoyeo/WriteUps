# Level01

## gremlin

### what does it do?
```bash
[gate@localhost gate]$ ./gremlin hello  
hello
```

첫 번째 커맨드 라인 인수를 출력하는 프로그램이다.

### source?
```c
/*
	The Lord of the BOF : The Fellowship of the BOF 
	- gremlin
	- simple BOF
*/
 
int main(int argc, char *argv[])
{
    char buffer[256];
    if(argc < 2){
        printf("argv error\n");
        exit(0);
    }
    strcpy(buffer, argv[1]);
    printf("%s\n", buffer);
}
```

## with GDB
```bash
[gate@localhost gate]$ gdb -q gremlin
(gdb) disass main
Dump of assembler code for function main:
0x8048430 <main>:	push   %ebp
0x8048431 <main+1>:	mov    %esp,%ebp
0x8048433 <main+3>:	sub    $0x100,%esp
0x8048439 <main+9>:	cmpl   $0x1,0x8(%ebp)
0x804843d <main+13>:	jg     0x8048456 <main+38>
0x804843f <main+15>:	push   $0x80484e0
0x8048444 <main+20>:	call   0x8048350 <printf>
0x8048449 <main+25>:	add    $0x4,%esp
0x804844c <main+28>:	push   $0x0
0x804844e <main+30>:	call   0x8048360 <exit>
0x8048453 <main+35>:	add    $0x4,%esp
0x8048456 <main+38>:	mov    0xc(%ebp),%eax
0x8048459 <main+41>:	add    $0x4,%eax
0x804845c <main+44>:	mov    (%eax),%edx
0x804845e <main+46>:	push   %edx
0x804845f <main+47>:	lea    0xffffff00(%ebp),%eax
0x8048465 <main+53>:	push   %eax
0x8048466 <main+54>:	call   0x8048370 <strcpy>
0x804846b <main+59>:	add    $0x8,%esp
0x804846e <main+62>:	lea    0xffffff00(%ebp),%eax
0x8048474 <main+68>:	push   %eax
0x8048475 <main+69>:	push   $0x80484ec
---Type <return> to continue, or q <return> to quit---                         
0x804847a <main+74>:	call   0x8048350 <printf>
0x804847f <main+79>:	add    $0x8,%esp
0x8048482 <main+82>:	leave  
0x8048483 <main+83>:	ret    
0x8048484 <main+84>:	nop    
0x8048485 <main+85>:	nop    
0x8048486 <main+86>:	nop    
0x8048487 <main+87>:	nop    
0x8048488 <main+88>:	nop    
0x8048489 <main+89>:	nop    
0x804848a <main+90>:	nop    
0x804848b <main+91>:	nop    
0x804848c <main+92>:	nop    
0x804848d <main+93>:	nop    
0x804848e <main+94>:	nop    
0x804848f <main+95>:	nop    
End of assembler dump.
(gdb) 
```

`sub $0x100,%esp`에서 스택 포인터(`esp`)를 움직임으로서 `0x100`의 메모리 공간을 확보한다.

```py
>>> 0x100
256
```

`0x100`은 `256`이다. 주어진 코드의 `char buffer[256];`를 통해서 `buffer`를 위해서 할당된 공간임을 알 수 있다.

추가로 `Stack Frame Pointer`(`SFP`)와 `Return address`(`RET`)가 각각 4바이트씩 차지할 것이다.

즉 프로그램의 스택 구조는 아래와 같을 것이다.

| RET [4]      |
| ------------ |
| SFP [4]      |
| buffer [256] |

프로그램의 실행 흐름을 바꾸기 위해서는 `buffer`에서 BOF를 일으켜 `RET`을 쉘코드의 주소로 변조하면 될 것이다.

즉 payload는 아무 문자 260개(`buffer[256] + SFP[4] = 260`) + 쉘코드 주소 => profit(아마)!!!
