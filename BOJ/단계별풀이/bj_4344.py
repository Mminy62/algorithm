
import sys

n = int(sys.stdin.readline())
data = []
m = [] #mean list
index = 0 #index of mean list 

for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

for d in data:
    mean = 0
    std_num = d[0]
    count = 0
    for i in range(1,std_num+1): #calculating the mean
        mean += d[i]
    
    mean = mean / std_num

    for i in range(1,std_num+1): #counting correct std
        if d[i] > mean:
            count += 1

            
    index += 1

    print("%.3f%%"% ((count/std_num)*100))
