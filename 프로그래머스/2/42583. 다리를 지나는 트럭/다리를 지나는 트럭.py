'''
15분~
모든 트럭이 다 건너는 최소 시간
bridge_length 개 최대 동시
weight 이하

'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = 0
    arrived = 0
    cur_weight = 0
    truck_weights = deque(truck_weights)
    
    q = deque([])
    # 초기 세팅
    
    while truck_weights and cur_weight + truck_weights[0] <= weight and len(q) < bridge_length:
        num = truck_weights.popleft()
        cur_weight += num
        q.append((num, time + bridge_length))
        time += 1
    
    
    # 시간에 따라 나갈 시간이 되면 내보내기
    while q:
        num, time = q.popleft()
        cur_weight -= num
        
        # 채우는 동안의 시간에 나갈 시간이 되면 내보내기 
        while truck_weights and cur_weight + truck_weights[0] <= weight and len(q) < bridge_length:
            # 채우는 동안에 나갈 시간의 트럭이 있으면 내보내기
            while q and q[0][1] == time:
                num, time = q.popleft()
                cur_weight -= num
                
            num = truck_weights.popleft()
            cur_weight += num
            q.append((num, time + bridge_length))
            time += 1

    return time + 1