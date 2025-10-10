'''
새정점이 어떤 것인지 찾고, 각각 어떤 것과 연결되어있는지 개수 파악할 것
'''
def solution(edges):
    n = 0 # 노드 수
    # [정점, 도넛, 막대, 8자]
    answer = [0, 0, 0, 0]
    total = 0
    size = set([])

    # n 구하는 과정
    for _, [a, b] in enumerate(edges):
        max_node = max(a, b)
        n = max(n, max_node)
        size.update([a, b])
    
    # meta [노드에 들어오는 간선의 개수, 노드로부터 나가는 간선의 개수]
    meta = [[0, 0] for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]

    # 방향이 있는 간선, a -> b
    for _, [a, b] in enumerate(edges):
        graph[a].append(b)
        meta[b][0] += 1
        meta[a][1] += 1

    # 그래프의 노드를 순회하면서 해당 노드의 이웃의 수가 2개 이상일 경우 탐색
    for i, [come, out] in enumerate(meta):
        if i not in size:
            continue
        # 시작 노드 / 나가는 정점 두개 이상, 들어오는 정점 없음
        if come == 0 and out >= 2:
            answer[0] = i
            total = len(graph[i])

        # 막대 그래프
        if come >= 0 and out == 0: # 나가는게 없는 정점을 찾는 것
            answer[2] += 1

        # 8자 그래프
        if come >= 2 and out == 2:
            answer[3] += 1

    answer[1] = max(total - answer[2] - answer[3], 0)
    return answer

