# BFS
from collections import deque
max_node = -1
def bfs(start_node):
    global n, max_node
    visited =[False]*(n+1)
    que = deque([[start_node,0]])
    visited[start_node]=True
    max_dist = 0

    while que:
        now, now_dist = que.popleft()
        for child,child_dist in data[now]:
            if not visited[child]:
                visited[child]=True
                que.append([child,now_dist+child_dist])
                if max_dist < now_dist+child_dist:
                    max_dist = now_dist+child_dist
                    max_node = child
    return max_dist

n = int(input())
if n == 1:
    print(0)
else:
    data = [[] for _ in range(n+1)]
    for _ in range(n-1):
        # 부모, 자식, 거리
        a,b,c = map(int,input().split())
        data[a].append([b,c])
        data[b].append([a,c])
    bfs(1)
    print(bfs(max_node))