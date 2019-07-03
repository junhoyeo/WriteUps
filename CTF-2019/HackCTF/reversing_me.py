serial = 'H`cjCUFzhdy^stcbers^D1_x0t_jn1w^r2vdrre^3o9hndes1o9>}'
flag = [chr((i%2) ^ ord(serial[i])) for i in range(len(serial))]
print(''.join(flag))
