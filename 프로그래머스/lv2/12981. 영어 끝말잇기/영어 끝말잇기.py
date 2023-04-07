import math

def solution(n, words):
    cnt = 0
    
    if len(words[0]) == 1:
        return [1, 1]
    
    for i in range(1, len(words)):
        pre = words[i-1]
        word = words[i]
        if pre[-1] != word[0] or word in words[:i] or len(word) == 1:
            if (i + 1) < n:
                mem = i + 1
                cnt = 1
            else:
                mem = (i + 1) % n
                if mem == 0:
                    mem = n
                cnt = math.ceil((i + 1) / n)
            break
        
    if cnt == 0:
        return [0, 0]
    else:
        return [mem, cnt]
