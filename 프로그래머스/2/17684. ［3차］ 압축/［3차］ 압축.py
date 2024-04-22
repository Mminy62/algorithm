def solution(msg):
    answer = []
    book = {}
    num = 27
    for i in range(1, 27):
        book[chr(64 + i)] = i
    start = 0
    
    # 사전에 있는 가장 긴 단어를 찾아야함
    idx = 0
    while idx < len(msg):
        keys = book.keys()
        stack = ''
        while idx < len(msg):
            stack += msg[idx]
            if stack in keys:
                idx += 1
            else:
                # 없는 것 기준으로 사전에 등록
                book[stack] = num
                num += 1
                break
        
        # 그 전 것 까지 정답에 넣기
        if idx == len(msg) or len(stack) == 1:
            answer.append(book[stack])
        else:
            answer.append(book[stack[:-1]])

    return answer
