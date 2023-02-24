from itertools import permutations
import math

def isPrime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
            
    
def solution(numbers):
    answer = 0
    result = []
    #숫자의 조합으로 소수인지 아닌지 파악
    
    num_list = list(numbers)
    com_list = []
    for i in range(1, len(numbers) + 1):
        temp = list(permutations(num_list, i))
    
        for data in temp:
            convert_int = int(''.join(map(str, data)))
            result.append(convert_int)
    
    #result
    for num in set(result):
        if isPrime(num):
            answer += 1
            
    return answer