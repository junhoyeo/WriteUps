def roman_to_int(roman):
    values = [
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}[c]
        for c in roman
    ]
    return sum(
        +n if n >= next else -n
        for n, next in zip(values, values[1:] + [0])
    )

with open('roman.txt', 'r') as f:
    msg = f.read().strip().replace('\n', ' ').split(' ')

roman = []
for word in msg:
    if word.isupper():
        roman.append(word)

flag = ''
for n in roman:
    flag += chr(roman_to_int(n))
print(flag)
