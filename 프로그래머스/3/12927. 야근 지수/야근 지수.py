import heapq

def solution(n, works):
    cnt = n
    answer = 0
    q = []
    for time in works:
        heapq.heappush(q, -time)
    
    for _ in range(n):
        item = -1 * heapq.heappop(q)
        if not q:
            break
        
        if item != 0:
            if item - 1 != 0:
                heapq.heappush(q, -(item - 1))
            cnt -= 1
    
    if not q:
        answer = 0
    else:
        for item in q:
            answer += item ** 2
    
    return answer
