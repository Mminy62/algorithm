arr = []
for _ in range(2):
    temp = list(map(int, input().split()))
    arr.append(sum(temp))
    
print(max(arr))