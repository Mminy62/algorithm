def solution(s):
    answer = []
    cnt0 = 0
    turn = 0
    
    while s != "1":
        turn += 1
        num = s.count("1")
        cnt0 += len(s) - num
        s = bin(num)[2:]
            

    return [turn, cnt0]