N = int(input())
info = []

for i in range(N):
    info.append(list(map(int,input().split(' '))))

for i in range(N):
    count = 1
    for j in range(N):
        if i != j:
            if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
                count += 1

    print(count, end=" ")