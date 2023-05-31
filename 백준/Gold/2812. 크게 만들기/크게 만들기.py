from collections import deque

n, k = map(int, input().split())

num = list(map(int, input()))

q = deque([num[0]])

for i in range(1, n):
    while k > 0 and q and q[-1] < num[i]:
        q.pop()
        k -= 1
    q.append(num[i])
    
if k > 0:
    for _ in range(k):
        q.pop()

print(''.join(map(str, q)))