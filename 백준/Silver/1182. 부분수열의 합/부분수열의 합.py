n, s = map(int, input().split())
array = list(map(int, input().split()))

cnt = 0
def dfs(idx, sub_sum):
    global cnt

    if idx >= n:
        return

    sub_sum += array[idx]

    if sub_sum == s:
        cnt += 1

    dfs(idx + 1, sub_sum)
    dfs(idx + 1, sub_sum - array[idx])

    return

dfs(0, 0)

print(cnt)