def solution(s):
    answer = 1
    stack = []
    
    for item in s:        
        if not stack:
            stack.append(item)
        else:
            if stack[-1] == item:
                stack.pop()
            else:
                stack.append(item)
    
    if not stack:
        return 1
    else:
        return 0