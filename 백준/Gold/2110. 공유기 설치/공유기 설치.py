import sys
array = []
n, c = map(int, sys.stdin.readline().split())
for _ in range(n):
    array.append(int(sys.stdin.readline()))
array.sort()

def binary_search(array, n, c):
    start = 1
    end = array[-1] - array[0]
    result = 0

    while start <= end:
        mid = (start + end)//2
        value = array[0]
        count = 1

        for i in range(1, n):
            if array[i] >= value + mid:
                value = array[i]
                count += 1
            if count == c:
                break
        if count >= c:
            start = mid + 1
            result = mid
        else:# count < c #gap 좀 낮추기
            end = mid - 1

    return result

print(binary_search(array, n, c))