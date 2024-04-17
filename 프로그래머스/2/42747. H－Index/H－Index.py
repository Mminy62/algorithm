from bisect import bisect_left
def solution(citations):
    answer = 0

    citations.sort()
    start = 0
    end = citations[-1]
    n = len(citations)
    
    while start <= end:
        mid = (start + end) // 2
        cnt = n - bisect_left(citations, mid)
        if cnt < mid:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid
    
    return answer