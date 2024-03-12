import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = {}
for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a] = [b, c]

def dfs1(root):
    cnt = 0
    a, b = graph[root]

    if a != -1:
        cnt += 2
        cnt += dfs1(a)

    if b != -1:
        cnt += 2
        cnt += dfs1(b)
    return cnt

def dfs2(root):
    cnt = 0
    b = graph[root][1]

    if b != -1:
        cnt += 1
        cnt += dfs2(b)
    return cnt

print(dfs1(1) - dfs2(1))