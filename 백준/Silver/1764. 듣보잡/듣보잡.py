import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s1 = set()
s2 = set()

for _ in range(n):
    s1.add(input())
for _ in range(m):
    s2.add(input())

result = list(sorted(s1 & s2))

print(len(result))
print(''.join(result))