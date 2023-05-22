import sys
input = sys.stdin.readline

n = int(input())
info = []
for _ in range(n):
    info.append(tuple(map(int, input().split())))

info.sort()

# L>R 인 순간에 놓으면 되니까 절반을 넘는 곳에 놓으면 된다.
prefix = [0] * n
prefix[0] = info[0][1]

for i in range(1, n):
    prefix[i] = prefix[i-1] + info[i][1]

for i in range(n):
    left = prefix[i]
    right = prefix[n-1] - prefix[i]
    if left >= right:
        print(info[i][0])
        break