a,b,c = map(int,input().split(" "))
if c - b > 0:
    re = a // (c - b)
    if re >= 0:
        print(re + 1)
    else:
        print(-1)
else:
    print(-1)
