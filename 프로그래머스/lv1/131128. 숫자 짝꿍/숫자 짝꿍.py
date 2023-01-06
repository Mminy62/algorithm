def solution(X, Y):
    result = []
    #공통인 수 뽑아서 (없으면 -1, 0만 있으면 0)역수로 정렬하고 join으로 string 리턴
    if X > Y : X, Y = Y, X #x < y
    
    n1 = [0] * 10
    n2 = [0] * 10
    
    for x in list(map(int,X)):
        n1[x] += 1
    
    for y in list(map(int,Y)):
        n2[y] += 1
        
    for i, (x, y) in enumerate(zip(n1, n2)):
        if x != 0 and y != 0:
            result.append(str(i)*min(x,y))
            
    if not result:
        return "-1"
    else:
        tmp = ''.join(sorted(result, reverse = True))
        return "0" if tmp[0] == "0" else tmp
