data = input()
temp = data[0]
result = 0

for i in range(1, len(data)):
    if temp != data[i]:
        result += 1
        temp = data[i]

print((result + 1)//2)