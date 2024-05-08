
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
from collections import deque


def solution(x, y, n):
    def bfs(x, y, n):
        q = deque()
        dist[x] = 1
        q.append(x)

        while q:
            x = q.popleft()
            if 0 <= x + n <= 1000000 and dist[x + n] == 0:
                dist[x + n] = dist[x] + 1
                q.append(x + n)
            if 0 <= x * 2 <= 1000000 and dist[x * 2] == 0:
                dist[x * 2] = dist[x] + 1
                q.append(x * 2)
            if 0 <= x * 3 <= 1000000 and dist[x * 3] == 0:
                dist[x * 3] = dist[x] + 1
                q.append(x * 3)

    dist = [0] * 1000001
    bfs(x,y,n)

    return dist[y]-1