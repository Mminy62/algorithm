from heapq import heappush, heappop
from collections import defaultdict
from math import inf

def solution(n, paths, gates, summits):
    gates, summits = set(gates), set(summits)
    A = defaultdict(list)
    for u, v, w in paths:
        A[u].append((v, w))
        A[v].append((u, w))
        
    intensity = [inf] + [inf] * n;
    q = []
    for g in gates:
        intensity[g] = 0
        heappush(q, (0, g))

    while len(q) > 0:
        inten, u = heappop(q)
        if inten > intensity[u] or u in summits:
            continue
        
        for v, w in A[u]:
            if intensity[v] > max(inten, w) and v not in gates:
                intensity[v] = max(inten, w)
                heappush(q, (max(inten, w), v))

    mn, mnsummit = inf, None
    for summit in sorted(summits):
        if intensity[summit] < mn:
            mn, mnsummit = intensity[summit], summit
                
    return mnsummit, mn