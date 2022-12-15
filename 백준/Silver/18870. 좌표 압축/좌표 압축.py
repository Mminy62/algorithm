def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None

n = int(input())
result = []
coors = list(map(int,input().split()))

temp = sorted(set(coors))


for target in coors:
    result.append(binary_search(target, temp))

print(*result, sep=' ') #줄바꿈없이 출력, 맨뒤에 \n도 출력 x 