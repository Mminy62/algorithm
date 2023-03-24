def solution(arr):
    answer = 0
    n = len(arr)
    mul = 1
    
    while True:
        cnt = 0
        mul += 1
        answer = arr[-1] * mul
        for i in range(0, n):
            if answer % arr[i] == 0:
                cnt += 1
                
        if cnt == n:
            break
            
    return answer