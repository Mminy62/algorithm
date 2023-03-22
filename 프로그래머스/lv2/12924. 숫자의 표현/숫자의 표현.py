def solution(n):
    answer = 0
    '''
    n은 연속한 자연수들로 표현할 수 있다. 
    n <= 10000
    cnt = 1
    
    '''
    cnt = 1
    for i in range(1, n//2 + 1):
        start = i
        temp = 0
        for k in range(start, n//2 + 2):
            temp += k
            if temp == n:
                cnt += 1
                break
            if temp > n:
                break

    return cnt