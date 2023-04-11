
'''
11:15-45

A가 올바른 괄호문자면 

AB도 올바른것

stack, pop 해서 올바른지 아닌지 확인
({})
'''
def solution(s):
    answer = 0
    
    left = ['(', '[', '{']
    right = [')', ']', '}']
    
    for x in range(len(s)):
        if x == len(s) - 1:
            temp = s[-1] + s[:x]
        else: 
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