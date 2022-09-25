N = input()
N = list(map(int,N))

for i in list(reversed(sorted(N))):
    print(i, end= "")