def solution(elements):
    answer = 0
    origin = elements
    telements = elements + elements
    
    n = len(origin)
    temp = set()
    for size in range(1, n + 1):
        for s in range(n):
            # 시작부터 size까지
            temp.add(sum(telements[s: s + size]))
    
    return len(temp)