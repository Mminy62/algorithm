def hanoi(n, a, c, answer):  # n개, a -> b
    if n == 0:
        return
    b = 6 - (a + c)
    hanoi(n - 1, a, b, answer)
    answer.append([a, c])
    hanoi(n - 1, b, c, answer)

    return answer

def solution(n):
    answer = []
    hanoi(n, 1, 3, answer)
    return answer
