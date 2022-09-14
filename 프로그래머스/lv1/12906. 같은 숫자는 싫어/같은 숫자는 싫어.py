def solution(arr):
    answer = []
    
    for data in arr:
        if not answer:
            answer.append(data)  
        else:
            if answer[-1] != data:
                answer.append(data)
            
    return answer


