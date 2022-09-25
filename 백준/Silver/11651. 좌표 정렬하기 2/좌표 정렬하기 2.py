N = int(input())

coor = {}

for i in range(N):
    x, y = map(int, input().split(' '))
    if y not in coor.keys():
        coor[y] = [x]
    else:
        coor[y].append(x)

#key is y value
for key, values in sorted(coor.items()):
    if len(values) > 1:
        for v in sorted(values):
            print(v, key)
    else:
        print(*values, key)