N = int(input())
arr = list(map(int, input().split()))

if sum(arr) % 3 == 0:
    temp = sum(arr) // 3
    two = 0
    for i in range(N): #two
        if arr[i] >= 2:
            two += arr[i] // 2
    if temp - two <= 0:
        print("YES")
    else:
        print("NO")

else:
    print("NO")