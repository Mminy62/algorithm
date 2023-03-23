def solution(A,B):
    answer = 0
    length = len(A)
    A.sort()
    B.sort()
    for _ in range(length):
        maxA, minA = A[-1], A[0]
        maxB, minB = B[-1], B[0]

        if maxA > maxB:
            max_value = maxA
            min_value = minB
            del A[-1]
            del B[0]
        else:
            max_value = maxB
            min_value = minA
            del A[0]
            del B[-1]

        answer += max_value * min_value
    

    return answer