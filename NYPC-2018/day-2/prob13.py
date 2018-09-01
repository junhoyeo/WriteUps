def swap(a, b):
    # usage : a, b = swap(a, b)
    return b, a

def rotation(matrix):
    # 외부 코드 사용 : https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python#answer-48950436
    wheel = list(zip(*reversed(matrix)))
    return [list(i)[::-1] for i in wheel][::-1]

n, t = [int(i) for i in input().split()]
matrix = [input().split() for i in range(n)]
for repeat in range(t):
    for i in range(0, n):
        for j in range(0, n-1):
            if matrix[i][j] > matrix[i][j+1]:
                matrix[i][j], matrix[i][j+1] = swap(matrix[i][j], matrix[i][j+1])
    matrix = rotation(matrix)
for i in matrix:
    print(*i)
