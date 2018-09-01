def binary_trees(n, i=0):
# https://stackoverflow.com/questions/24076440/how-to-list-all-the-possible-binary-search-trees-with-n-nodes#answer-24084749
    if not n: return [[]]
    else:
        ll=[]
        for k in range(n):
            l1 = binary_trees(k, 2*i+1)
            l2 = binary_trees(n-1-k, 2*i+2)
            for j in l1:
                for l in l2:
                    ll.append([i]+j+l)
        return ll

def layer_nodes(h):
    node = 1
    layer = 0
    prev = 0
    l = []
    while layer <= h:
        if layer != 0:
            l = list(range(prev, node))
        prev = node
        node *= 2
        layer += 1
    return [i-1 for i in l]

n, h = [int(i) for i in input().split()]
node_num = 2 ** h - 1
# print('node_num', node_num)
l = binary_trees(n)
layer_n = layer_nodes(h)
# print('layer', layer_n)
count = 0
for n_tree in l:
    if all(node < node_num for node in n_tree) and (max(n_tree) in layer_n):
        # print(n_tree)
        count += 1
print(count%1000000007)
