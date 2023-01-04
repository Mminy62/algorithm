def solution(x, n):
    return [x]*n if x == 0 else list(range(x, x*(n+1), x))