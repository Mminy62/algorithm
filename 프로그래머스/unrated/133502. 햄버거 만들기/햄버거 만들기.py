def solution(ingredient):
    answer = 0
    stack = []
    top = 0
    
    for i in ingredient:
        if len(stack):
            top = stack[-1]
            
        stack.append(i)
        
        if i == 1 and len(stack) > 3:
            if stack[-4:] == [1,2,3,1]:
                del stack[-4:]
                answer += 1
                
    return answer