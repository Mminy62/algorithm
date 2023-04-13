def dfs(n, m, s):
    if len(s) == m and s == sorted(s):
        return print(*s, sep=' ')

    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs(n, m, s)
            s.pop()
    return

n, m = map(int, input().split())
s = []
dfs(n, m, s)