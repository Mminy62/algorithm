def solution(t, p):
    temp = []
    
    for i in range(len(t[len(p)-1:])):
        temp.append(int(t[i:i+len(p)]))
    p = int(p)
    return len(list(filter(lambda x: x <= p, temp)))