N, K = map(int, input().split())

N_unit = []
for i in range(N):
    N_unit.append(int(input()))

mok = 0
coin = 0

for i in reversed(N_unit):
    if K > 0:
        mok = K // i

        if mok != 0:
            coin += mok
            K -= mok * i
            
print(coin)
