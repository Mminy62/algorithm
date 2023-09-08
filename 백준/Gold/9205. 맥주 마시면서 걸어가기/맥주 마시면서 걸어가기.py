from collections import deque
import math
tc = int(input())

for _ in range(tc):
    n = int(input())
    conv = []
    home = tuple(map(int, input().split()))
    for _ in range(n):
        conv.append(tuple(map(int, input().split())))
    fest = tuple(map(int, input().split()))
    visited = [False] * n
    ans = ''
    '''
    1. 현재 지점에서 축제지점까지의 거리
    2. 안되면 근처 편의점으로 추적
    '''
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([home])
    while q:
        x, y = q.popleft()
        fx, fy = fest
        if abs(fx - x) + abs(fy - y) <= 1000:
            ans = 'happy'
            break
        else:
            for i in range(n):
                if abs(x - conv[i][0]) + abs(y - conv[i][1]) <= 1000 and not visited[i]:
                    visited[i] = True
                    q.append((conv[i][0], conv[i][1]))
    if not ans:
        ans = 'sad'

    print(ans)