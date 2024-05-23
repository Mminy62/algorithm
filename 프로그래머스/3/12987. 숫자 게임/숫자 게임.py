from bisect import bisect_left

def solution(A, B):
    answer = 0
    
    B.sort()
    
    for item in A:
        idx = bisect_left(B, item + 1) 
        if idx == len(B):
            continue
        del B[idx]
        answer += 1
    
    return answer