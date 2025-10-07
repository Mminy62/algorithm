def solution(n, m, section):
    answer = 0
    end = 0
    
    for sec in section:
        if sec > end:
            answer += 1
            end = sec + m - 1
    
    return answer