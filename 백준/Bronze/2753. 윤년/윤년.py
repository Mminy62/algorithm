year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    answer = 1
else:
    answer = 0
print(answer)