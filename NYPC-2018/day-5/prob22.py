from collections import namedtuple
Rect = namedtuple('Rect', 'x1 y1 x2 y2')

# def intersects(r1, r2):
#     return not (r1[2][0] < r2[4][0] or r1[4][0] > r2[2][0] or r1[]
#     or self.top_right.y < other.bottom_left.y 
#     or self.bottom_left.y > other.top_right.y)

colored = []

def area(a, b):
    # 참고 : https://stackoverflow.com/questions/40795709/checking-whether-two-rectangles-overlap-in-python-using-two-bottom-left-corners#answer-40795835
    # print(a, b)
    dx = min(a.x2, b.x2) - max(a.x1, b.x1)
    dy = min(a.y2, b.y2) - max(a.y1, b.y1)
    if (dx >= 0) and (dy >= 0):
        return Rect(max(a.x1, b.x1), max(a.y1, b.y1), min(a.x2, b.x2), min(a.y2, b.y2))
    return None

def separate(rect):
    for x in range(rect.x1, rect.x2 + 1):
        for y in range(rect.y1, rect.y2 + 1):
            print(x, y)

n = int(input())
rect = [[int(j) for j in input().split()] for i in range(n)]
blue = []
red = []
for i in range(n):
    if rect[i][4] == 1:
        red.append(
            Rect(rect[i][0], rect[i][1], rect[i][2], rect[i][3])
        )
    else:
        blue.append(
            Rect(rect[i][0], rect[i][1], rect[i][2], rect[i][3])
        )
print('red', *red)
print('blue', *blue)
for i in red:
    for j in blue:
        a = area(i, j)
        print(a)
        separate(a)
