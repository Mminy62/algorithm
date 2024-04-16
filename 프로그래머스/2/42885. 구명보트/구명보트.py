from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people, key=lambda x: -x))
    remains = 0
    
    while len(people) > 1:
        left = people.popleft()
        
        right = people[-1]
        
        remain = limit - left
        if remain >= right:
            people.pop()
            answer += 1
        else:
            remains += 1
        
    if len(people):
        answer += 1
    answer += remains
        
    return answer