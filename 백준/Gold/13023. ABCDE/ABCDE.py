from collections import defaultdict
n, m = map(int, input().split())

# a, b, c, d, e가 되는지 각 시작점마다 확인 => 2000개 * 2000 10 ** 6
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

people = graph.keys()
answer = False
visited = []
def dfs(start, stack):
    global answer
    global visited
    if len(stack) == 5:
        answer = True
        return

    for friend in graph[start]:
        # notin
        if not visited[friend]:
            visited[friend] = True
            dfs(friend, stack + [friend])
            visited[friend] = False

    return


for start in people:
    visited = [False] * n
    visited[start] = True
    stack = [start]
    dfs(start, stack)
    if answer:
        break

if answer:
    print(1)
else:
    print(0)