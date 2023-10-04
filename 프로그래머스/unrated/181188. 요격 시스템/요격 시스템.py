def solution(targets):
#     targets.sort(key=lambda x: (x[0], x[1]))

#     cnt = 0
#     end = -1
#     for i in range(len(targets)):
#         s, e = targets[i][0], targets[i][1]
#         if end <= s:
#             cnt += 1
#             end = e
#         else:# 같은 라인
#             end = min(end, e)

    targets.sort(key=lambda x:x[1])
    cnt = 0
    end = -1
    for s, e in targets:
        if end <= s:
            cnt += 1
            end = e

    return cnt