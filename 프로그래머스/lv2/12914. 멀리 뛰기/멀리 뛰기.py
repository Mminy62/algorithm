from math import comb
def solution(n):#~2시까지
    answer = 1
    for i in range(1, n//2 + 1): # i 는 2의 개수
        cnt2 = n - i * 2
        numbers = i + cnt2
        answer += comb(numbers, i)
    
    return answer % 1234567