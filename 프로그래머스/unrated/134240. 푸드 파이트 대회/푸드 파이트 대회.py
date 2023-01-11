def solution(food):
    answer = ''
    for i, v in enumerate(food):
        if v >= 2:
            answer += str(i)*(v//2)
    answer += str(0) + (answer[::-1])
    
    return answer