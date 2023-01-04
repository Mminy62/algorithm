def solution(num):
    cnt = 0

    while(cnt < 501):
        if num == 1:
            return cnt
        
        num = num / 2 if not num % 2  else (num * 3 + 1)
        
        cnt += 1
    
    return -1