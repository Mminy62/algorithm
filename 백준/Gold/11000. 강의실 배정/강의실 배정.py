import heapq
n = int(input())
classes = []
room = []
cnt = 0

for _ in range(n):
    classes.append(list(map(int, input().split())))

classes.sort()
heapq.heappush(room, classes[0][1])

for i in range(1, n):
    if room[0] <= classes[i][0]:
        heapq.heappop(room)
        heapq.heappush(room, classes[i][1])
    else:
        heapq.heappush(room, classes[i][1])

print(len(room))