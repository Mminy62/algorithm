from itertools import permutations
n = int(input())

a = list(map(int, input().split()))

op_num = list(map(int, input().split()))
op_list = ''
for i in range(4):
    op_list += str(i) * op_num[i]

operators = set(permutations(list(op_list), n-1))

max_res = -10**9
min_res = 10**9
for operator in operators:
    temp = a[0]
    for i, op in enumerate(operator):
        op2 = a[i+1]
        if op == '0':
            temp += op2
        if op == '1':
            temp -= op2
        if op == '2':
            temp *= op2
        if op == '3':
            if temp < 0:
                temp = abs(temp) // op2
                temp = -temp
            else:
                temp = temp // op2
    max_res = max(temp, max_res)
    min_res = min(temp, min_res)

print(max_res)
print(min_res)