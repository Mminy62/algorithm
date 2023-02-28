import sys
input = sys.stdin.readline

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))


ropes.sort(reverse=True)
weight = ropes[0]

for i in range(1, len(ropes)):
    temp = ropes[i] * (i+1)
    if temp >= weight:
        weight = temp

print(weight)