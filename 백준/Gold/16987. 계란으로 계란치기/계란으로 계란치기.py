import sys
input = sys.stdin.readline

n = int(input())

egg_info = []
answer = 0

for _ in range(n):
    egg_info.append(list(map(int, input().split())))


def dfs(now):
    global answer

    # 전부 깨진 경우 or now == n
    if now == n:
        broken_cnt = 0
        for i in range(n):
            if egg_info[i][0] <= 0:
                broken_cnt += 1
        answer = max(answer, broken_cnt)
        return

    # 내가 깨진 경우
    if egg_info[now][0] <= 0:
        dfs(now + 1)
        return

    #나 빼고 다 깨진 경우
    broken_all = True
    for i in range(n):
        if i == now:
            continue
        if egg_info[i][0] > 0:
            broken_all = False
            break
    if broken_all:
        answer = max(answer, n - 1)
        return

    # 2번 - 깨는 과정
    for target in range(n):
        if target == now:
            continue
        if egg_info[target][0] <= 0: continue
        if egg_info[target][0] > 0:
            # 깨기
            egg_info[now][0] -= egg_info[target][1]
            egg_info[target][0] -= egg_info[now][1]
            dfs(now + 1)
            # 복구
            egg_info[now][0] += egg_info[target][1]
            egg_info[target][0] += egg_info[now][1]

dfs(0)
print(answer)