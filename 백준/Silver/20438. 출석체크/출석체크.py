import sys
input = sys.stdin.readline
N, K, Q, M = map(int, input().split())

ks = set(map(int, input().split()))
qs = set(map(int, input().split()))
ms = []
for _ in range(M):
    s, e = map(int, input().split())
    ms.append((s, e))

visited = [0] * (N + 3)
for q in (qs - ks):
    for i in range(q, N + 3, q):
        if i not in ks:
            visited[i] = 1

attend = [0] * (N + 3)
for i in range(3, N + 3):
    if not visited[i]:
        attend[i] = attend[i-1] + 1
    else:
        attend[i] = attend[i-1]

answer = []
for s, e in ms:
    answer.append(attend[e] - attend[s-1])

for a in answer:
    print(a)