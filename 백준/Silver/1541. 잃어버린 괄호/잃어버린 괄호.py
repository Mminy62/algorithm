import re
strings = input()
ops = re.split('[0-9]+', strings)[1:-1]
nums = list(map(int, re.split('[-+]', strings)))

result = 0
i = len(nums)
if '-' in strings:
    i = ops.index('-')

result = sum(nums[:i+1]) - (sum(nums[i+1:]))
print(result)