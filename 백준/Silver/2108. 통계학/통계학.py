import sys
from collections import Counter

N = int(input())

arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

#평균
result = []
result.append(round(sum(arr)/N))

#중앙값
result.append(arr[N//2])

#최빈값
cnt = Counter(arr)
temp = cnt.most_common()
if len(temp) > 1 and temp[0][1] == temp[1][1]:
    result.append(temp[1][0])
else: 
    result.append(temp[0][0])

#result.append(mode)
result.append(arr[N-1]-arr[0])

for i in result:
    print(i)
