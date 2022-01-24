data = input().upper()

dic_data = {} #'B':2
cnt = 0

for i in set(data):
    dic_data[i] = data.count(i)

for k,v in dic_data.items():
     if v == max(dic_data.values()):
         cnt += 1
         char = k

if cnt == 1:
    print(char)
else:
    print("?")
