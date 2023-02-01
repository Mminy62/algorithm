n = list(map(int, input()))

be = n[0:len(n)//2]
af = n[len(n)//2:]

if sum(be) == sum(af):
    print("LUCKY")
else:
    print("READY")