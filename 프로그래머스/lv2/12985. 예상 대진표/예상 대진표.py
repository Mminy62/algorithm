def solution(n,a,b):
    answer = 0

    for _ in range(n//2):
        a = a // 2 + 1 if a % 2 else a // 2
        b = b // 2 + 1 if b % 2 else b // 2
        answer += 1

        if a == b:
            break

    return answer