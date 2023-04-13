n, m = map(int, input().split())

array = list(map(int, input().split()))
array.sort()
s = []

def dfs():
    if len(s) == m and s == sorted(s):
        print(*s, sep=' ')
        return
    elif len(s) == m:
        return

    for i in range(n):
        s.append(array[i])
        dfs()
        s.pop()

    return
dfs()