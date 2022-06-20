num = int(input())

count = 1
temp = 1
i = 0

while num > temp:
    i += 1
    temp += 6 * i
    count += 1


print(count)
