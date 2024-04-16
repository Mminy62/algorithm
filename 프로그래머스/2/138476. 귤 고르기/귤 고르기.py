from bisect import bisect_left
from collections import Counter

def solution(k, tangerine):
    answer = 0
    dictionary = Counter(tangerine)
    items = sorted(dictionary.values())

    while k > 0:
        idx = bisect_left(items, k)

        if idx == len(items):
            idx -= 1

        k -= items[idx]
        answer += 1
        items.pop(idx)
        
    return answer