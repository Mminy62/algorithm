n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dist = []
node = []

def dfs():
    
    if len(node) > 1 and graph[node[-2]][node[-1]] == 0:
        return

    if len(node) == n:
        if graph[node[-1]][node[0]] == 0:
            return
        temp = 0
        for i in range(n-1):
            temp += graph[node[i]][node[i+1]]
        temp += graph[node[-1]][node[0]]
        dist.append(temp)
        return

    for i in range(n):
        if i not in node: # and graph[node[-1]][j]
            node.append(i)
            dfs()
            node.pop()

dfs()
print(min(dist))