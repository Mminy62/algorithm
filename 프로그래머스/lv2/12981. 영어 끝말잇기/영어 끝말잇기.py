import math

def solution(n, words):
    cnt = 0
    
    if len(words[0]) == 1:
        return [1, 1]
    
    for i in range(1, len(words)):
        pre = words[i-1]
        word = words[i]
        if pre[-1] != word[0] or word in words[:i] or len(word) == 1:
            mem = (i % n) + 1
            cnt = i // n + 1
            break
        
    if cnt == 0:
        return [0, 0]
    else:
        return [mem, cnt]
