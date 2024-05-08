from collections import deque
def solution(order):
    answer = 0    
    n = len(order)
    first = deque([i for i in range(1, n + 1)])
    second = []
    
    for num in order:
        # 먼저 first를 체크하고 거기에 해당되면 찾고, 아니면 second로 넘긴다
        if first and num >= first[0]:
            while first:
                box = first.popleft()
                if num != box:
                    second.append(box)
                else:
                    answer += 1
                    break
            
        else:
            box = second.pop()
            if num == box:
                answer += 1
                continue
            else:
                break
                    
    return answer