n, m = map(int, input().split())

s = []

def dfs():
    if len(s) == m and s == sorted(s):
        print(*s, sep=' ')
        return
    elif len(s) == m:
        return

    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()

    return

dfs()