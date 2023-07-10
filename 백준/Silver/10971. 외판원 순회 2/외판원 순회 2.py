n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
node = []
min_dist = 1e9

def dfs():
    global min_dist

    if len(node) > 1 and graph[node[-2]][node[-1]] == 0:
        return

    if len(node) == n and graph[node[-1]][node[0]] != 0:
        temp = 0
        for i in range(n-1):
            temp += graph[node[i]][node[i+1]]
        temp += graph[node[-1]][node[0]]
        min_dist = min(min_dist, temp)
        return

    for i in range(n):
        if i not in node:# and graph[node[-1]][j]
            node.append(i)
            dfs()
            node.pop()


dfs()
print(min_dist)