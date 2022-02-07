import sys

        
num = int(sys.stdin.readline())

for i in range(num):
    k = int(input())
    n = int(input())

    a = []
    
    for i in range(1,n+1):
        a.append(i) 

    for j in range(k):
        for i in range(1,n):
            a[i] += a[i-1]

    print(a[n-1])
