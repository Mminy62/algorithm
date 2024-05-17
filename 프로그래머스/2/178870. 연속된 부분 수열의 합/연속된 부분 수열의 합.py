'''
임의의 두 인덱스의 원소, 그 사이 원소를 모두 포함하는 부분 수열
부분 수열의 합은 k
합이 k인 부분 수열이 여러개인 경우 길이가 짧은 수열을 찾는다 
길이가 짧은게 여러개면, 시작인덱스가 작은걸로 찾기 
시작, 마지막 인덱스를 담은 배열을 return 
'''

def solution(sequence, k):
    start = 0
    end = 0
    n = len(sequence)
    tmp = sequence[start]
    answer = [0, n + 1]
    
    while end < n and start <= end:
        if tmp == k and answer[1] - answer[0] > end - start:
            answer = [start, end]
            tmp -= sequence[start]
            start += 1
        
        elif tmp > k:
            tmp -= sequence[start]
            start += 1
        else: # tmp < k
            end += 1
            if end > n - 1:
                break
            tmp += sequence[end]
            
        
    return answer