def solution(n):
    #answer = sorted(list(map(int, str(n))), reverse=True)
    return int(''.join(sorted(str(n), reverse=True)))