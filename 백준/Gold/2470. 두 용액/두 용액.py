n = int(input())
array = list(map(int, input().split()))

array.sort(key=abs)
diff = []
ans = 1e9

for i in range(1, n):
    temp = array[i] + array[i-1]
    diff.append((temp, i)) # i, i-1

diff.sort(key=lambda x: abs(x[0]))

index = diff[0][1]
ans = [array[index], array[index-1]]
print(*sorted(ans))