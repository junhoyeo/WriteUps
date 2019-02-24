# 멀웨어 유형 

## Fileless malware 📁❌
저장 장치에 악성 파일을 저장하지 않고, RAM에 로드되어 실행 ➡️ 안티바이러스 회피 

- 기존의 파일리스 멀웨어는 그 특성상 재부팅 때까지가 수명(일회성)
- 재부팅 후에도 다시 동작하기 위해서 종료 명령이 들어오면 ... (Methods to maintaining persistence)
  - 시스템(레지스트리 등)에 악성코드를 저장 부팅 시 실행하고 파일 삭제 
  - 암호화된 멀웨어를 다시 다운로드해서 실행

- http://blog.naver.com/aepkoreanet/220934328454
- https://github.com/codeengn/codeengn_conference/blob/master/14/2017%20CodeEngn%20Conference%2014,%20Fileless%20악성코드%20기법과%20종류%20[차민석].pdf

## Ransomware 📁💰
파일을 암호화하거나 시스템 접근을 제한하고 금전을 요구

1. 대상 검색
   암호화할 파일을 검색한다. 사용자의 활동을 미리 모니터링해서 이를 선별하기도 한다.
2. 파일 암호화
3. 복구 방식 전달
   Tor와 비트코인을 이용해서 추적이 어렵게 한다.

- Crypt
  - **CryptoLocker**
- Cerber
- Locker
- MBR
- Other
  - **WannaCry**
  - GANDCRAB

## Dropper ⬇️📦
트로이 목마의 일종으로 다른 멀웨어를 시스템에 설치하기 위해서 사용됨

- 안티바이러스를 회피하기 위해서 드로퍼에 멀웨어 코드를 숨겨 설치함
- 또는 드로퍼가 실행되면서 인터넷에서 다운로드 받아 설치됨

- Meredrop
- Destover-C
