from itertools import combinations
def solution(numbers):
    answer = []
    
    return sorted(list(set(map(lambda x : sum(x), combinations(numbers,2)))))