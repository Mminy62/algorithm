import re
expr = input()
nums = list(map(int, re.split('[-+]', expr)))
ops = re.split('[0-9]', expr)
ops = list(filter(lambda x: x != '', ops))

result = nums[0]

for i in range(1, len(ops)):
    if ops[i-1] == '-' and ops[i] == '+':
        ops[i] = '-'

for i in range(len(ops)):
    if ops[i] == '-':
        result -= nums[i + 1]
    else:
        result += nums[i + 1]

print(result)