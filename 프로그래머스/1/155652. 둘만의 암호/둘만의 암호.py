def solution(s, skip, index):
    answer = ''
    sample = ''.join(chr(i) for i in range(97, 123) if chr(i) not in skip)
    
    for c in s:
        idx = sample.index(c)
        idx = (idx + index) % len(sample)
        answer += sample[idx]

    return answer