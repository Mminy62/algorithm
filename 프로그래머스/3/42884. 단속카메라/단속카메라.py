def solution(routes):
    answer = 1
    routes.sort()
    maxv, minv = routes[0][0], routes[0][1]
    print(maxv, minv)
    n = len(routes)
    for i in range(1, n):
        max2, min2 = routes[i]
        if maxv <= max2 and max2 <= minv:
            maxv, minv = max2, min(min2, minv)
        else:
            answer += 1
            maxv, minv = max2, min2
    
    return answer
