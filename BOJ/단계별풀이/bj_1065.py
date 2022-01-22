import sys

x = int(sys.stdin.readline())
hansu = 0
temp = 0
for num in range(1,x+1):
    if num < 100:
        hansu += 1
    else: #len(num) > 2
        num_list = list(map(int,str(num)))
        diff = num_list[1] - num_list[0]

        for i in range(len(str(num))-1):
            if diff == (num_list[i+1] - num_list[i]):
                temp += 1
            if temp == len(str(num))-1:
                hansu += 1
        temp = 0

print(hansu)
