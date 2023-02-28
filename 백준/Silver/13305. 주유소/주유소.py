import sys
input = sys.stdin.readline

city_num = int(input())
distance = list(map(int, input().split()))
citys = list(map(int, input().split()))
result = 0
citys.pop()

min_index = citys.index(min(citys))
if min_index == 0:
    result = citys[0] * sum(distance)
else:
    while min_index != 0:
        result += citys[min_index] * sum(distance[min_index:])

        distance = distance[:min_index]
        citys = citys[:min_index]
        min_index = citys.index(min(citys))

    result += citys[0] * distance[0]

print(result)