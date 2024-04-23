def number_list(num, n):
    result = ''
    alpha = 'ABCDEF'
    if num == 0:
        return '0'
    
    while num > num // n:
        tmp = num % n
        if tmp > 9:
            tmp = alpha[tmp - 10]
        else:
            tmp = str(tmp)
            
        result = tmp + result
        num = num // n
    if num:
        result = str(num) + result
    
    return result

def solution(n, t, m, p):
    answer = ''
    # n진법에 따른 숫자 구하기 
    stack = ''
    num = 0
    
    while len(stack) <= t * m:
        stack += number_list(num, n)
        num += 1
    
    # t*m개까지 stack을 채워놓고 -> 간격만큼 순서를 건너뛰면서 result 채우기
    size = (m - p) + p
    
    cnt = 0
    for i in range(p - 1, t * m, size):
        if cnt == t:
            break
        answer += stack[i]
        cnt += 1
    
    return answer