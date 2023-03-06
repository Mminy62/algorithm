import heapq

def solution(food_times, k):
    answer = 0
    
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    
    #이전에 더한 값
    sum_value = 0
    previous_value = 0
    length = len(food_times)
    count = 0

    while sum_value + (q[0][0] - previous_value) * length <= k:
        now, i = heapq.heappop(q)
        sum_value += (now - previous_value) * length
        previous_value = now
        length -= 1

    q = sorted(q, key = lambda x: x[1])

    return q[(k-sum_value) % length][1]