def solution(targets):
    targets.sort(key=lambda x: (x[0], x[1]))

    cnt = 1
    end = targets[0][1]
    for i in range(1, len(targets)):
        s, e = targets[i][0], targets[i][1]
        if end <= s:
            cnt += 1
            end = e
        else:# 같은 라인
            end = min(end, e)
    print(cnt)
    return cnt