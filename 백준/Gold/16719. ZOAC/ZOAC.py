name = input()
name_list = list(enumerate(name))

starts = [-1]
result = []
start = starts[-1]
end = len(name)
result_string = ''
while starts:# starts가 빌때까지
    if start + 1 == end:
        starts.pop()
        end = start
        if starts:
            start = starts[-1]
        continue

    temp = name_list[start + 1: end]
    temp.sort(key=lambda x: (x[1], x[0]))
    start = temp[0][0]
    starts.append(start)
    result.append(name_list[start])
    result.sort(key=lambda x: x[0])
    result_string = ''.join(t[1] for t in result)
    print(result_string)