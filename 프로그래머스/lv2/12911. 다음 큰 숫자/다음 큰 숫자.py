def solution(n):
    answer = 0
    '''
    
    n의 다음 큰 숫자는 n보다 큰 자연수이다. 
    n의 다음 큰 숫자와 n은 2진수로 변환했을 때의 1의 갯수가 같다.
    n이 110 이면 큰 숫자는 1100
    
    + 1씩 늘려가면서 1의 갯수가 같아지면 stop
    
    '''
    flag = bin(n).count('1')
    
    while True:
        n += 1
        if bin(n).count('1') == flag:
            answer = n
            break
            
    return answer