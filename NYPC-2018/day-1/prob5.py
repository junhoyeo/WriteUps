with open('input5.5.txt', 'r') as f:
    n = int(f.readline())
    for i in range(n):
        print(''.join([word[0] for word in f.readline().split()]))
