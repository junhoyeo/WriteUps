# def binary_trees(n, i=0):
# # https://stackoverflow.com/questions/24076440/how-to-list-all-the-possible-binary-search-trees-with-n-nodes#answer-24084749
#     if not n: return [[]]
#     else:
#         ll=[]
#         for k in range(n):
#             l1 = binary_trees(k, 2*i+1)
#             l2 = binary_trees(n-1-k, 2*i+2)
#             for j in l1:
#                 for l in l2:
#                     ll.append([i]+j+l)
#         return ll

# def layer_nodes(h):
#     node = 1
#     layer = 0
#     prev = 0
#     l = []
#     while layer <= h:
#         if layer != 0:
#             l = list(range(prev, node))
#         prev = node
#         node *= 2
#         layer += 1
#     return [i-1 for i in l]

# n, h = [int(i) for i in input().split()]
# node_num = 2 ** h - 1
# # print('node_num', node_num)
# l = binary_trees(n)
# layer_n = layer_nodes(h)
# # print('layer', layer_n)
# count = 0
# for n_tree in l:
#     if all(node < node_num for node in n_tree) and (max(n_tree) in layer_n):
#         # print(n_tree)
#         count += 1
# print(count%1000000007)

# 위와 같은 코드와 pwntools를 이용해서 N<=10일 경우의 수를 모두 구해서 딕셔너리를 만들고 조회하는 방법으로 문제를 해결합니다.

key = [(1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)]
ans = [0, 1, 0, 0, 2, 0, 0, 1, 4, 0, 0, 0, 6, 8, 0, 0, 0, 6, 20, 16, 0, 0, 0, 4, 40, 56, 32, 0, 0, 0, 1, 68, 152, 144, 64, 0, 0, 0, 0, 94, 376, 480, 352, 128, 0, 0, 0, 0, 114, 844, 1440, 1376, 832, 256, 0, 0, 0, 0, 116, 1744, 4056, 4736, 3712, 1920, 512]
n, k = [int(i) for i in input().split()]
print(ans[key.index((n, k))])
