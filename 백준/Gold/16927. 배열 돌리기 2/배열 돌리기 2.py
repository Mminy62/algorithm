from collections import deque
import sys
input = sys.stdin.readline
N, M, R = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

def search(rs, re, cs, ce):
    # 순환 방향대로
    temp = deque([])
    #왼쪽 아래
    for i in range(rs, re):#N-1까지 맞지, N-2까지로 돌려야하니까
        temp.append(arr[i][cs])
    # 아래
    temp += arr[re][cs:ce]
    # 오른쪽 아래서 위로
    for i in range(re, rs, -1):
        temp.append(arr[i][ce])
    # 위, 오른쪽에서 왼쪽으로
    temp += reversed(arr[rs][cs + 1:ce + 1])

    return temp

def arrange(result, temp, rs, re, cs, ce):
    # 순환 방향대로
    # 왼쪽 아래
    for i in range(rs, re):  # N-1까지 맞지, N-2까지로 돌려야하니까
        result[i][cs] = temp.popleft()
    # 아래
    for i in range(cs, ce):
        result[re][i] = temp.popleft()

    # 오른쪽 아래서 위로
    for i in range(re, rs, -1):
        result[i][ce] = temp.popleft()

    # 위, 오른쪽에서 왼쪽으로
    for i in range(ce, cs, -1):
        result[rs][i] = temp.popleft()
    return result

result = [[0] * M for _ in range(N)]
row = min(N, M) // 2
starts = deque([(i, i) for i in range(row)])

while starts:
    rs, cs = starts.popleft()
    re, ce = N - rs - 1, M - cs - 1
    temp = search(rs, re, cs, ce)
    temp.rotate(R)
    result = arrange(result, temp, rs, re, cs, ce)

# 재배치
# 위 아래에서 밑으로
for i in range(N):
    print(' '.join(map(str, result[i])))