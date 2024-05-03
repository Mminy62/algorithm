def solution(n, s):
    answer = []
    while n:
        num = s // n
        s -= num
        n -= 1
        answer.append(num)
        if num == 0:
            answer = [-1]
            break
    return sorted(answer)
