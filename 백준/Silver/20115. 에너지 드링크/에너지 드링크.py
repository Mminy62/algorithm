n = int(input())

array = list(map(int, input().split()))

array.sort()
result = array[-1] + (array[0]/2)

for i in range(1, n-1):
    result += (array[i]/2)

print(result)