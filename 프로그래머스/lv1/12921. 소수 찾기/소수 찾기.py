def eratos(n):
    table = [True] * (n+1)
    
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if table[i] == True: #소수
            for j in range(i+i, n+1, i):
                table[j] = False #배수 지우기
    
    return [i for i in range(2, n+1) if table[i] == True]
            
    
def solution(n):
    
    return len(eratos(n))