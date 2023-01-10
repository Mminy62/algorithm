def solution(a, b, n):
    answer = 0
    #a가 짝수이면 짝수만큼의 빈명만 만들어서 가져가고 나머지가 없을때까지 하는 것
    # 나누기 2한 것만 받을 수 있는 병의 수 
    
    while(n >= a):
        answer += (n // a) * b
        n = n - (n//a)*a + ((n//a)*b)
        
        
    return answer