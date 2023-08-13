from collections import deque
num = int(input())

nodes = [[] for _ in range((num + 1))]
max_node = 0
for _ in range(num):
    temp = deque(list(map(int, input().split()))[:-1])
    a = temp.popleft()

    while temp:
        b = temp.popleft()
        c = temp.popleft()
        nodes[a].append((b, c))
        nodes[b].append((a, c))

# 우선 루트에서 가장 멀리 떨어진 노드를 찾는다.
def BFS(root):
    global max_node

    visited = [False] * (num + 1)
    queue = deque([(root, 0)])
    max_dist = 0
    visited[root] = True

    while queue:
        now, now_dist = queue.popleft()
        for child, child_dist in nodes[now]:
            if not visited[child]:
                visited[child] = True
                queue.append((child, now_dist + child_dist))
                if max_dist < now_dist + child_dist:
                    max_dist = now_dist + child_dist
                    max_node = child
    return max_dist

BFS(1)
print(BFS(max_node))