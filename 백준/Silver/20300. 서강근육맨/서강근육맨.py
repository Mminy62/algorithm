n = int(input())

loss = list(map(int, input().split()))
loss.sort()
rloss = sorted(loss, reverse=True)

m = 0

if n % 2 != 0:
    m = rloss[0]
    del rloss[0]

for i in range(n // 2):
    temp = loss[i] + rloss[i]
    if temp > m:
        m = temp

print(m)