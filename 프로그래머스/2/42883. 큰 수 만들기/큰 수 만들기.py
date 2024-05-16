def solution(number, k): 
    stack = []
    for i in range(len(number)):
        if stack and stack[-1] < number[i]:
            while stack and stack[-1] < number[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(number[i])
        
        else:
            stack.append(number[i])
    
    if k > 0:
        while k > 0:
            stack.pop()
            k -= 1
    
    return ''.join(stack)
