enc = ['0', '>', '\x13', '(', '\x15', '\x17', '\x10', '6', '{', '\x1b', 'y', '\x17', '\x1c', '6', 'F', '3', '1', '\x1a', '(', '5', '>', 'b', '\x1f', '*', '\x02', 'X', 'H', '(', '\x01', '\x00', '\n', '\x1f', '>', '!', 'S', ',', '\x1f', '\r', '\x1c', '6', '5', '%', '\t', '\x07', '.', '>', '\x08', 'J', '\x14', '\x14', '%', '\x1f', '6', '%', 's', '\x18', '\x0b', '2', 't', '\x08', 'J', '\x14', '6']
print(len(enc))
Dst = []
for i in range(100):
    Dst.append(0)
byte_4045E0 =
for i in range(64):
    try:
        Dst[i] = ord(byte_4045E0[i % 13]) ^ ord(enc[i])
    except: break
print([chr(c) for c in Dst])