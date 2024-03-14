n, m = map(int, input().split())
array = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    temp = array[a:b + 1][::-1]
    array[a:b + 1] = temp

print(" ".join(map(str, array[1:])))