from bisect import bisect_left

def solution(k, tangerine):
    answer = 0
    size_dict = {}
    for i in range(len(tangerine)):
        item = tangerine[i]
        if item not in size_dict.keys():
            size_dict[item] = 1
        else:
            size_dict[item] += 1
    
    items = sorted(size_dict.values())

    while k > 0:
        idx = bisect_left(items, k)

        if idx == len(items):
            idx -= 1

        k -= items[idx]
        answer += 1
        items.pop(idx)
        
    return answer