def solution(x):
    # answer = map(int,str(x))
    # if x % sum(answer) == 0:
    #     return True
    # else:
    #     return False
    return x % sum([int(c) for c in str(x)]) == 0