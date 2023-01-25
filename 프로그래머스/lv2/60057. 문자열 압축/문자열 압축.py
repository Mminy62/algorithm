def solution(s):
    length = len(s)
    temp = s
    before = 0
    answer = []

    if length <= 1:
        return length
    
    #문자열 끊는 단위
    for i in range(1, length):
        count = 1
        result = ''

        for j in range(0, length, i): #i 만큼 끊어서 표현
            cur = temp[j:j + i]

            if (j + i) >= length:#현재 값이 넘어가나 마지막인 경우
                if before == cur:
                    result += str(count+1) + before

                else: #before != cur
                    if count > 1:
                        result += str(count) + before + cur
                    else:# count == 1
                        result += before + cur

            else:
                if j == 0:# 초기값
                    before = cur

                elif before == cur:
                    count += 1

                else:#before != cur
                    if count == 1:
                        result += before
                    else:
                        result += str(count) + before

                    count = 1
                    before = cur

        answer.append((i, len(result)))

    d = sorted(answer, key = lambda x : x[1])
    
    return d[0][1]