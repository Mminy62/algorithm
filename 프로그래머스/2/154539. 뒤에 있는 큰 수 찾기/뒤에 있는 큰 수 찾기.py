'''
현재 값보다 이전에 작은 값들이 있었으면 빼준다. 
정해지지 않은 값들을 일단 갖고 있다가.
자기보다 작은 값이었는데 answer로 정해지지 않은 것은 값을 부여한다. 

'''
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
        
    return answer