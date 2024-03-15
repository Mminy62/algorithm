def KMP(pattern):
    lp = len(pattern)
    table = [0] * lp
    pidx = 0
    for idx in range(1, lp):
        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = table[pidx - 1]

        if pattern[idx] == pattern[pidx]:
            pidx += 1
            table[idx] = pidx

    return table

T = input().rstrip()
P = input().rstrip()
n = len(T)
m = len(P)
table = KMP(P)
pidx = 0
result = []

for idx in range(n):

    while pidx > 0 and T[idx] != P[pidx]:
        pidx = table[pidx - 1]


    if T[idx] == P[pidx]:
        if pidx == m - 1:
            result.append((idx - m + 2))
            pidx = table[pidx]
        else:
            pidx += 1

print(len(result))
print(' '.join(map(str,result)))