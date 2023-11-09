N = int(input())

A, B, C, D = [], [], [], []
for _ in range(N):
    temp = list(map(int, input().split()))
    A.append(temp[0])
    B.append(temp[1])
    C.append(temp[2])
    D.append(temp[3])

arrAB = []
arrCD = []

for i in range(N):
    for j in range(N):
        arrAB.append(A[i] + B[j])

for i in range(N):
    for j in range(N):
        arrCD.append(C[i] + D[j])

arrAB.sort()
arrCD.sort()


i = 0
j = len(arrCD) - 1
cnt = 0

while i < len(arrAB) and j >= 0:
    temp = arrAB[i] + arrCD[j]
    if temp == 0:
        nexti = i + 1
        nextj = j - 1
        while nexti < len(arrAB) and arrAB[nexti] == arrAB[i]:
            nexti += 1
        while nextj >= 0 and arrCD[nextj] == arrCD[j]:
            nextj -= 1

        cnt += abs(nexti - i) * abs(nextj - j)
        i = nexti
        j = nextj

    elif temp > 0:
        j -= 1
    else:
        i += 1

print(cnt)

