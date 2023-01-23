import heapq
def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))  
    
    sumvalue = 0
    previous = 0
    length = len(food_times)
    
    while sumvalue + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sumvalue += (now - previous) * length
        length -= 1
        previous = now
        
    result = sorted(q, key = lambda x:x[1])
    return result[(k - sumvalue) % length][1]