def solution(s):
    answer = True
    
    
    if s[0] == ')' or s[-1] == '(': #우선 앞이 ) , 뒤가 (로 끝나면 안됨 false
        return False
    else:
        stack = list(s)
    
    
    temp = 0
    for data in stack:
        if data == '(':
            temp += 1
        else:
            temp -= 1
        
        if temp < 0: #중간에 -1 이 나오면 바로 false
            return False
    
    if temp == 0: #최종 합이 0이어야 true
        return True
    else:
        return False
        

    return answer