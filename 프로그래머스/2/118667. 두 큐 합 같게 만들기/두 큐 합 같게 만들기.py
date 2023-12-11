from collections import deque

def solution(queue1, queue2):
    answer = -2
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    target = sum(queue1) + sum(queue2)
    if target % 2:
        return -1
    target /= 2

    maxCount = len(queue1) * 2 * 2
    moveCount = 0
    sum1, sum2 = sum(queue1), sum(queue2)

    while moveCount < maxCount:
        if target == sum1:
            return moveCount

        if target > sum1:
            # 하나 빼기  => 이진탐색이네,
            temp = queue2.popleft()
            queue1.append(temp)
            sum1 += temp
            sum2 -= temp

        else:# target < sum1
            temp = queue1.popleft()
            queue2.append(temp)
            sum1 -= temp
            sum2 += temp

        moveCount += 1

    return -1

