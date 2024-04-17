def solution(elements):
#     origin = elements
#     telements = elements + elements
    
#     n = len(origin)
#     temp = set()
#     for size in range(1, n + 1):
#         for s in range(n):
#             # 시작부터 size까지
#             temp.add(sum(telements[s: s + size]))

    n = len(elements)
    result = set()
    for i in range(n):
        ssum = elements[i]
        result.add(ssum)
        for j in range(i + 1, i + n):
            ssum += elements[j % n]
            result.add(ssum)
    
    return len(result)