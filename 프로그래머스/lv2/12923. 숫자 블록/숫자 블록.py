def solution(begin, end):
    answer = []
    for i in range(begin, end + 1):
        k = int(i != 1)
        for j in range(2, int(i ** 0.5) + 1):
            if i > 10 ** 7 and i % j == 0:
                k = j
            if i % j == 0 and i // j <= 10 ** 7:
                k = i // j
                break
        answer.append(k)
        
    return answer