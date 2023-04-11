def solution(s):
    answer = 0
    
    left = ['(', '[', '{']
    right = [')', ']', '}']
    
    for x in range(len(s)):
        temp = s[x:] + s[:x]
        stack = [temp[0]]
        
        for i in range(1, len(temp)):
            if temp[i] in left:
                stack.append(temp[i])
            else:#right
                index = right.index(temp[i])
                if stack and left[index] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(temp[i])
        
        if not stack:
            answer += 1
        
    return answer