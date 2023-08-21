from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

one, two = map(int, input().split())

result = 0
def bfs(weight):
    visited = [False] * (n + 1)
    visited[one] = True
    q = deque([one])

    while q:
        cur = q.popleft()
        for node, dist in graph[cur]:
            if not visited[node] and dist >= weight:
                q.append(node)
                visited[node] = True

    if visited[two]:
        return True
    return False

# 중량 제한 자체를 이분탐색
start, end = 0, 1000000000

while start <= end:
    mid = (start + end) // 2
    if bfs(mid):# 통과
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)