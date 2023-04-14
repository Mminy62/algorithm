n, m, k = map(int, input().split())
array = []
index = []
s = []
store = []

for _ in range(n):
    array.append(list(map(int, input().split())))

def dfs(r, c):
    if len(s) == k:
        value = sum(s)
        store.append(value)
        return

    for i in range(r, n):
        for j in range(c if i == r else 0, m):
            if (i, j) not in index and (i-1, j) not in index and (i+1, j) not in index and (i, j-1) not in index and (i, j+1) not in index:
                s.append(array[i][j])
                index.append((i, j))
                dfs(i, j)
                s.pop()
                index.pop()

dfs(0, 0)
print(max(store))