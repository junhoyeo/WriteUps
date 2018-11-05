chrs = "#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
flag = ['?' for i in range(25)]
loc = [
    (0 ,36),
    (9, 74),
    (18, 60),
    (12, 66),
    (4, 69),
    (24, 53),
    (6, 62),
    (7, 65),
    (16, 82),
    (23, 59),
    (22, 59),
    (19, 33),
    (1, 76),
    (2, 60),
    (11, 72),
    (13, 60),
    (21, 54),
    (14, 54),
    (5, 66),
    (20, 62),
    (10, 62),
    (15, 76),
    (3, 17),
    (8, 60),
    (17, 47)
]
for i, j in loc:
    flag[i] = chrs[j]
print(''.join(flag))
# Go_4head_make_YouR_DaY^^X
