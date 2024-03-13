from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
finder = {}

for _ in range(N + M):
    a, b, c = input().rstrip().split()

    if a not in finder:
        finder[a] = set()
    finder[a].add((b, c))

n = int(input())
for _ in range(n):
    query = list(input().rstrip().split("/"))
    cnt = 0
    total_cnt = 0
    folder_cnt = 0
    temp = set()

    # query안에 있는 폴더들의 깊이
    q = deque([query[-1]])

    while q:
        key = q.popleft()
        if key not in finder.keys():
            continue
        # 폴더에 파일이 있는 경우

        for item in finder[key]:
            if item[1] == "1":
                q.append(item[0])
                folder_cnt += 1

        total_cnt += len(finder[key])
        temp = temp | finder[key]

    cnt = len(temp) - folder_cnt
    total_cnt -= folder_cnt

    print(cnt, total_cnt)