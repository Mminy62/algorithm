n = int(input())
crains = list(map(int, input().split()))

m = int(input())
boxes = list(map(int, input().split()))

crains.sort(reverse=True)
boxes.sort(reverse=True)

time = 0
if boxes[0] > crains[0]:
    time = -1

else:
    while boxes:
        for i in range(n):
            for j in range(len(boxes)):
                if crains[i] >= boxes[j]:
                    del boxes[j]
                    break
        time += 1

print(time)