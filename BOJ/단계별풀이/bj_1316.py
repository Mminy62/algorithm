import sys

n = int(sys.stdin.readline().rstrip())

input_data = []
re = ""
group = []


for i in range(n):
    input_data.append(sys.stdin.readline().rstrip())

for k in input_data:
    temp = []
    for i in range(int(len(k))):
        if i == 0 or k[i] not in temp:
            temp.append(k[i])
            
        else:
            if k[i-1] == k[i]:
                 temp.append(k[i])
                 
    if k == re.join(temp):
        group.append(k)

print(len(group))
