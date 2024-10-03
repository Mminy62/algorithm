import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    N, M = M, N
    pos = deque([])
    visited = {}
    
    def dfs(x, y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return
        if (x, y) not in visited.keys():
            return
        if visited[(x, y)]:
            return
        visited[(x, y)] = True
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return

    for _ in range(K):
        c, r = map(int, input().split())
        pos.append((r, c))
        visited[(r, c)] = False
 
    cnt = 0
    while pos:
        x, y = pos.popleft()
        if not visited[(x, y)]:
            dfs(x, y)
            cnt += 1

    print(cnt)