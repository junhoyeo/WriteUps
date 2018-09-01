with open('drill', 'r') as f:
    data = f.read()
data = [int(data[i:i+2], 16) for i in range(0, len(data), 2)]
text = ''
for i in data:
    text += chr(i)
print(text)
# print(data) 