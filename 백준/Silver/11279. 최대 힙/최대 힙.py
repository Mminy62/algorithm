import heapq
import sys

input = sys.stdin.readline

n = int(input())
queue = []
for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(queue, -num)
    else:
        if not queue:
            print(0)
        else:
            print(-heapq.heappop(queue))