n = int(input())
result = 0
array = list(map(int, input().split()))
prefix_sum = 0
for i in range(len(array)-1):
    prefix_sum += array[i]
    result += prefix_sum * array[i + 1]

print(result)