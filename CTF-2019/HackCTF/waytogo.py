with open('./14E-0', 'rb') as f:
  data = f.read()
with open('./new.png', 'wb') as f:
  f.write(bytes(reversed(data)))
