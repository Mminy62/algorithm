import heapq
def solution(operations):
    answer = []
    q = []
    for cmds in operations:
        cmd, num = cmds.split()
        if cmd == "D" and q:
            if num == "-1":
                heapq.heappop(q)
            else:
                q.pop()
        if cmd == "I":
            heapq.heappush(q, int(num))
    
    if not q:
        return [0, 0]
    else:
        answer = [max(q), min(q)]
    
    return answer