import sys
input  = sys.stdin.readline

K, L = map(int, input().split())
array = {}

for _ in range(L):
    temp = input().rstrip()
    if temp not in array.keys():
        array[temp] = 1
    else:
        array.pop(temp)
        array[temp] = 1

keys = list(array.keys())
cnt = K if len(keys) > K else len(keys)

for i in range(cnt):
    print(keys[i])