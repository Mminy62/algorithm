def solution(s):
    answer = 0
    x = 0
    y = 0
    start = 0
    
    for i, c in enumerate(s):
        if not start:
            start = c
            x += 1
        elif start == c:
            x += 1
        else:
            y += 1
        
        if x == y:
            x, y = 0, 0
            start = 0
            answer += 1
    
    if start != 0:
        answer += 1
            
    return answer