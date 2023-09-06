import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
stack = deque([])

def dfs(cur, cnt):
    global result

    if cnt == 5:
        result = 1
        return

    for next in graph[cur]:
        if next not in stack:
            stack.append(next)
            dfs(next, cnt + 1)
            stack.pop()

    return

for i in range(n):
    stack.append(i)
    dfs(i, 1)
    if result:
        break
    stack.pop()

print(result)