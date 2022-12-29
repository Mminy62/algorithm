def solution(arr, divisor):
    answer = []
    
    answer = list(filter(lambda x: x % divisor == 0, arr))
    
    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    
    return answer