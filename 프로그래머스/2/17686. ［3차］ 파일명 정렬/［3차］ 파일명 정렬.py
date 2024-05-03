import heapq
def solution(files):
    answer = []
    q = []
    for idx, file_name in enumerate(files):
        digitFlag = False
        head = ''
        number = ''
        tail = ''
        cnt = 0
        for i, c in enumerate(file_name):
            if not c.isdigit() and not digitFlag:
                head += c.lower()
            else:
                digitFlag = True
                if cnt < 5 and c.isdigit():
                    cnt += 1
                    number += c
                else:
                    break
                    
        number = int(number)
        tail = idx
        heapq.heappush(q, (head, number, tail, file_name))
        
    while q:
        answer.append(heapq.heappop(q)[-1])
    
    return answer