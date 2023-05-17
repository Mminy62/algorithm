import sys
import heapq
input = sys.stdin.readline

n = int(input())
lines = []
heap = []
for i in range(n):
    lines.append(tuple(map(int, input().split())))
    
lines.sort()
maxLen = 0

for s, e in lines:
    while heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, e)
    if maxLen < len(heap):
        maxLen = len(heap)
print(maxLen)