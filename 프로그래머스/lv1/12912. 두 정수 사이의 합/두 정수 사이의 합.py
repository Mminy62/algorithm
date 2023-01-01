def solution(a, b):
    answer = 0
    
    if a > b:
        temp = a
        a = b
        b = temp
        
    for s in range(a,b+1):
        answer += s
    return answer