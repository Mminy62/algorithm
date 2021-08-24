import sys

time = []
count = 0
total = 0

n = int(input())

for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    time.append([a,b])


time.sort()

for a,b in time:
    if a < total:
        if b < total:
            total = b

    else:# a>= total # cut line
        total = b
        count += 1

print(count)
