import heapq
def solution(scoville, K):
    answer = 0
        
    if K == 0:
        return 0
    
    q = []
    for item in scoville:
        heapq.heappush(q, item)
    
    # 0번째 item의 값이 K이상인경우 멈추기
    while q[0] < K:
        if len(q) < 2:
            return -1
        item1 = heapq.heappop(q)
        item2 = heapq.heappop(q)
        new = item1 + (item2 * 2)
        heapq.heappush(q, new)
        answer += 1

    return answer
