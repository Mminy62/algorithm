count = 0

n = int(input())

res = 100
comp = n

if n >= 0 and n < 100:
    
    while res != n:
        if comp >= 10:
            str_tmp = str(comp) #26 -> '26'
            num_tmp = int(str_tmp[0]) + int(str_tmp[1]) #2+6 = 8
            num_tmp = str(num_tmp)
            comp = int(str_tmp[1] + num_tmp[-1])
            
        else:
            num_tmp = comp
            comp = int(str(comp)*2)

        count += 1
        res = comp
        
print(count)
