import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
maps = []
for _ in range(H):
    maps.append(list(map(int, input().split())))

if (W, H) == (1, 1):
    print(0)
else:
    q = deque([(0, 0, K)])
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx2 = [-1, 1, 0, 0]
    dy2 = [0, 0, -1, 1]
    
    visited = [[[False] * W for _ in range(H)] for _ in range(K + 1)]
    for i in range(K + 1):
        visited[i][0][0] = True
    dist = [[0] * W for _ in range(H)]
    dist[H - 1][W - 1] = -1
    temp = []
    
    
    def move(cur, nx, ny, k_cnt):
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            return False
        if maps[nx][ny] == 1:
            return False
        if maps[nx][ny] == 0 and not visited[k_cnt][nx][ny]:
            visited[k_cnt][nx][ny] = True
            dist[nx][ny] = cur + 1
    
        if (nx, ny) == (H - 1, W - 1):
            temp.append(cur + 1)
        # true 이면 k_cnt 를 낮춰야하나?
        return nx, ny, k_cnt
    
    
    while q:
        x, y, k = q.popleft()
        if k > 0:
            for i in range(8):
                hx = x + dx[i]
                hy = y + dy[i]
    
                if hx < 0 or hx >= H or hy < 0 or hy >= W or maps[hx][hy] == 1:
                    continue
                if maps[hx][hy] == 0 and not visited[k-1][hx][hy]:
                    visited[k-1][hx][hy] = True
                    dist[hx][hy] = dist[x][y] + 1
                    q.append((hx, hy, k-1))
    
                if (hx, hy) == (H-1, W-1):
                    temp.append(dist[x][y] + 1)
    
        # 원숭이 움직임은 매번
        for i in range(4):
            mx, my = x + dx2[i], y + dy2[i]
    
            if mx < 0 or mx >= H or my < 0 or my >= W or maps[mx][my] == 1:
                continue
    
            if maps[mx][my] == 0 and not visited[k][mx][my]:
                visited[k][mx][my] = True
                dist[mx][my] = dist[x][y] + 1
                q.append((mx, my, k))
    
            if (mx, my) == (H - 1, W - 1):
                temp.append(dist[x][y] + 1)
    
    if temp:
        dist[H - 1][W - 1] = min(temp)
    
    print(dist[H - 1][W - 1])