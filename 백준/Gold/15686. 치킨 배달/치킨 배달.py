from itertools import combinations

n, m = map(int, input().split())

road = []
home = []
store = []

for i in range(n):
    road.append(list(map(int, input().split())))
#home, store 좌표
for i in range(n):
    for j in range(n):
        if road[i][j] == 1:
            home.append((i, j))
        elif road[i][j] == 2:
            store.append((i, j))


result = []
com_store = list(combinations(store, m))

for data in com_store: #((1,2), (2,3))
    com_distance = 0  # 조합당 distance

    for r1, c1 in home:#한 집에서 제일 가까운 치킨집에 거리
        home_distance = n * n
        for r2, c2 in data:  # 1개의 조합 치킨집을 다 돌고 최소값 구하기
            temp = abs(r2 - r1) + abs(c2 - c1)
            if home_distance > temp:
                home_distance = temp

        com_distance += home_distance

    result.append(com_distance)

print(min(result))