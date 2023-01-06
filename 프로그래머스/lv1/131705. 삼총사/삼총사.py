from itertools import combinations

def solution(number):

    return len(list(filter(lambda x: sum(x) == 0, combinations(number, 3))))
