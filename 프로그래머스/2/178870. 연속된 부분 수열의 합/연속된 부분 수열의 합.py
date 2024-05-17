# 누적합 풀이
def solution(sequence, k):
    answer = [0, 10 ** 6]
    n = len(sequence)
    prefix = [0] * (n)
    tmp = 0
    for i in range(1, n):
        tmp += sequence[i]
        prefix[i] = tmp

    start = 0
    end = 0
    tmp = 0
    while end < n and start <= end:
        tmp = prefix[end] - prefix[start] + sequence[start]
        if tmp > k:
            start += 1
        elif tmp < k:
            end += 1
        else:
            if answer[1] - answer[0] > end - start:
                answer = [start, end]
            end += 1
                
    return answer