def solution(s):
    answer = []
    cnt0 = 0
    turn = 0
    
    while True:
        turn += 1
        cnt0 += s.count("0")
        s = s.replace("0", "")
        length = len(s)

        s = bin(int(length))
        if s == bin(1):
            answer = [turn, cnt0]
            break
        else:
            s = s[2:]
            

    return answer