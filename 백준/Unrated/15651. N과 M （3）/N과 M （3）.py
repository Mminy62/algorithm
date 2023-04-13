n, m = map(int, input().split())
s = []

def dfs():
    if len(s) == m:
        print(*s, sep=' ')
        return

    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()

    return

dfs()