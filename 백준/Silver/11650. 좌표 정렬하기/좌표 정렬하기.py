N = int(input())

coor = {}

for i in range(N):
    x, y = map(int, input().split(' '))
    if x not in coor.keys():
        coor[x] = [y]
    else:
        coor[x].append(y)

for key, values in sorted(coor.items()):
    for value in sorted(values):
        print(key, value)