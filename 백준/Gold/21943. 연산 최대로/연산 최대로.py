import sys

si = sys.stdin.readline


def MIIS(): return map(int, si().split())


n = int(si())
lst = sorted(MIIS())
p, q = MIIS()
answer = 0
'''
곱하기 개수 + 1개 덩어리로 나누어서 각 수의 곱이 최대로 하는 값 찾기
곱하기 개수 + 1개의 덩어리로 나누는 경우의 수를 전부 찾는다.
--> 조합으로 경우의 수 찾아내고 dfs로 max값 갱신시켜나간다. 
'''
# arr에서 r개를 뽑는 조합


def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], r-1):
                yield next + [arr[i]]

# dfs로 구현


def dfs(arr, count, now):
    # 곱하기가 0이 들어오면 남은 숫자 전부 더하면 된다.
    if count == 0:
        global answer
        answer = max(answer, now * sum(arr))
        return now * sum(arr)
    # 들어온 arr의 인덱스를 가지는 리스트
    idx = range(len(arr))
    for i in range(1, len(arr) - count + 1):
        # j는 [0,1,2,3,4,5]에서 i개를 뽑는 경우의 수
        for j in combinations(idx, i):
            temp = arr[:]
            # print(f"temp = {temp}")
            # 현재 조합의 합을 들어온 이전 결과에 곱해준다.
            multiple_to = 0
            # 인덱스를 기준으로 뽑아내서 담는다.
            for k in j:
                multiple_to += temp.pop(k)
            # print(f"temp_sum = {multiple_to}")
            # 복사한 리스트, 덩어리 하나 선택, 현재 곱셈한 결과 보냄
            dfs(temp, count - 1, now * multiple_to)
    return answer


answer = dfs(lst, q, 1)
print(answer)