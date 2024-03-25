A, B = map(int, input().split())
result = []
def dfs(origin, cnt):
    if origin > B:
        return -1
    if origin == B:
        return cnt
    else:

        result1 = dfs(origin * 2, cnt + 1)
        temp = str(origin) + '1'
        result2 = dfs(int(temp), cnt + 1)
        if result1 == -1 and result2 == -1:
            return -1
        elif result1 == -1 or result2 == -1:
            return max(result1, result2)
        else:
            return min(result1, result2)


print(dfs(A, 1))