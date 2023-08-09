import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N = int(input())
Tree = {}
for i in range(N):
    Tree[i] = []

first = 0 # top root
parent = list(map(int, input().split()))
re_node = int(input())

for i, v in enumerate(parent):
    if v == -1:#top root
        first = v
    else:
        Tree[v].append(i)

def remove(root):
    for node in Tree[root]:
        if not Tree[node]:
            Tree.pop(node)
        else:
            remove(node)
    Tree.pop(root)

remove(re_node)


cnt = 0
for key in Tree.keys():
    if re_node in Tree[key]:
        Tree[key].pop(Tree[key].index(re_node))
    if not Tree[key]:
        cnt += 1

print(cnt)