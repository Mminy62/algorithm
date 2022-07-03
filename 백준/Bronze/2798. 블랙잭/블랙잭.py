from itertools import combinations

num, cond = map(int,input().split(' '))

s_list = []

cards = map(int,input().split(' '))

case = list(combinations(cards, 3))

for i in case:#i == list format
    temp = sum(i)
    if temp <= cond:# sum-> sum list items
        s_list.append(temp)
        
        
print(max(s_list))