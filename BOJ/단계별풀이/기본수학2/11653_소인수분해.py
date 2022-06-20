num = int(input())

if num != 1:
    for i in range(2,num+1):
        while num % i == 0:
            num //= i
            print(i)
        
else:
    print()
