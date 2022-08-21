M = int(input())

lenM = len(str(M))


tempN = M - (lenM * 9)

if tempN < 0:
    tempN = 0
    ran = M
else:
    ran = lenM * 9

for i in range(ran):
    genNum = tempN + i
    tempResult = genNum
    genNumDigit = list(map(int, str(genNum)))
    for data in genNumDigit:
        tempResult += data

    if tempResult == M:
        print(genNum)
        break
    elif i == (ran-1):
        print("0")