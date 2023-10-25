def solution(n, times):
    answer = 0
    times.sort()
    
    start = times[0]
    end = times[-1] * n
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for time in times:
            cnt += mid // time
        
        if cnt >= n:
            answer = mid
            end = mid - 1
        
        else:
            start = mid + 1
    
    
    return answer

