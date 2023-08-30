n = int(input())
array = list(map(int, input().split()))

idp = [1] * n
ddp = [0] * n

for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            idp[i] = max(idp[j] + 1, idp[i])


for i in range(n-1, -1, -1):
    for k in range(i+1, n):
        if array[k] < array[i]:
            ddp[i] = max(ddp[i], ddp[k] + 1)

# 1000번
result = 0
for i in range(n):
    result = max(ddp[i] + idp[i], result)

print(result)
