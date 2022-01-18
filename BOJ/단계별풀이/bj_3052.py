import sys


data = []

for _ in range(10):
    a = int(sys.stdin.readline())
    data.append(a % 42)

print(len(set(data)))
