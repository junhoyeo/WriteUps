s = "9P&;gFD,5.BOPCdBl7Q+@V'1dDK?qL"
for i in range(256):
    flag = ''.join([chr(ord(c) ^ i) for c in s])
    print(flag)
    