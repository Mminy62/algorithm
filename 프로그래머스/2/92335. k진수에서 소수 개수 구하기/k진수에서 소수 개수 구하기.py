def check_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True
        
def solution(n, k):
    answer = 0
    temp = ''
    n = int(n)
    while n // k > k:
        temp = str(n % k) + temp
        n = n // k
        
    result = str(n // k) + str(n % k) + temp
    
    length = len(result)
    tmp = result[0]

    for i in range(1, length):
        if result[i] != '0':
            tmp += result[i]
        else:
            if tmp and check_prime(int(tmp)):
                answer += 1
            tmp = ''

    if tmp and check_prime(int(tmp)):
        answer += 1
    
    return answer
