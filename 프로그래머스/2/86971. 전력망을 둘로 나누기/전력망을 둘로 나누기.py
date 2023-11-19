from collections import deque
from copy import deepcopy

def solution(n, wires):
    answer = n

    # 101개로 늘려주기
    graph = [[] for _ in range(101)]

    # wire 하나를 끊을때마다 갖게 되는 양옆 트리의 노드 갯수
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # delete
    for dv1, dv2 in wires:
        temp_graph = deepcopy(graph)

        temp_graph[dv1].remove(dv2)
        temp_graph[dv2].remove(dv1)

        visited = [False] * 101
        q = deque([])
        q.append(dv1)

        v1cnt = 0
        while q:
            node = q.popleft()

            if not visited[node]:
                v1cnt += 1
                visited[node] = True

                for item in temp_graph[node]:
                    if not visited[item]:
                        q.append(item)

        q.append(dv2)
        v2cnt = 0
        while q:

            node = q.popleft()

            if not visited[node]:
                v2cnt += 1
                visited[node] = True

                for item in graph[node]:
                    if not visited[item]:
                        q.append(item)

        answer = min(answer, abs(v1cnt - v2cnt))

    return answer