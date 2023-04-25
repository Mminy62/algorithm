import sys
input = sys.stdin.readline

n, k = map(int, input().split())
childs = list(map(int, input().split()))
result = 0
gap = []
for i in range(1, n):
    gap.append(childs[i] - childs[i-1])

gap.sort()
result += sum(gap[:n-k])
print(result)