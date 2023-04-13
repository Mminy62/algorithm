n, m = map(int, input().split())

array = list(map(int, input().split()))
array.sort()
s = []

def dfs():
    if len(s) == m:
        print(*s, sep=' ')
        return

    for i in range(n):
        s.append(array[i])
        dfs()
        s.pop()

    return

dfs()