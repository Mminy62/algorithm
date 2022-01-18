import sys

n = int(sys.stdin.readline())
data = list( map(int,sys.stdin.readline().split()) )

M = max(data)
result = 0


for s in data:
    result += s/M*100

print(result/n)
