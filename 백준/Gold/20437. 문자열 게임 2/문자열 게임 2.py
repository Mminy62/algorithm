import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().rstrip()
    k = int(input())

    info = [[] for _ in range(26)]
    temp = list(set(s))
    min_ans, max_ans = 10001, 0


    for i in range(len(s)):
        info[ord(s[i]) - 97].append(i)

    for i in range(26):
        if len(info[i]) < k:
            continue
        else: #탐색 시작
                # 3번, 4번 -> 최소길이
            min_length = 10001
            max_length = 0
            start = 0
            end = 0 + k - 1
            while end < len(info[i]):
                min_length = min(min_length, info[i][end] - info[i][start] + 1)
                max_length = max(max_length, info[i][end] - info[i][start] + 1)
                start += 1
                end += 1

            min_ans = min(min_ans, min_length)
            max_ans = max(max_ans, max_length)

    if min_ans == 10001 or max_ans == 0:
        print(-1)
    else:
        print(min_ans, max_ans)