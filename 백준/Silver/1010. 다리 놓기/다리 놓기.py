k = int(input())
for _ in range(k):
    n, m = map(int, input().split())
    dam = 1
    
    for i in range(n):
        dam *= m - i
        dam //= i + 1

    print(dam)