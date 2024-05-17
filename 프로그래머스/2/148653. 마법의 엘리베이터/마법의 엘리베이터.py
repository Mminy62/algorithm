'''
각각 비교하는데, 
끝자리가 5인경우, ㅇ바로 왼쪽 수가 과반수 초과면, 더해주고
과반수 이하이면, 빼준다 

끝자리가 5보다 밑인경우, 그냥 빼준다(옆숫자와 상관없이)
끝자리가 5보다 위인경우, 그냥 더해준다 (옆숫자와 상관없이)
'''

def solution(storey):
    answer = 0
    arr = list(map(int, str(storey)))
    n = len(arr)
    
    while storey:
        if len(str(storey)) == 1:
            if storey > 5:
                answer += (10 - storey)
                answer += 1
            else:
                answer += storey
            break
        
        remain = storey % 10
        pre = int(str(storey)[-2])
        if remain > 5:
            storey += (10 - remain)
            answer += (10 - remain)
        if remain < 5:
            storey -= remain
            answer += remain
        if remain == 5:
            if pre >= 5:
                storey += 10
            answer += 5  
        
        storey //= 10   
        
    return answer

