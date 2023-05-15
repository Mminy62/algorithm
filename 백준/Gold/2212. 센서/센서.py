n = int(input())
k = int(input())

sensors = list(map(int, input().split()))
sensors.sort()
diff = []
for i in range(1, n):
    diff.append(sensors[i] - sensors[i-1])

diff.sort()

print(sum(diff[:(n-1)-(k-1)]))