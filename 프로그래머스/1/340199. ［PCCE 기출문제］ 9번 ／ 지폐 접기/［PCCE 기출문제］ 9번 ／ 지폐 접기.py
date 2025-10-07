'''
항상 길이가 긴쪽을 반으로 접는다
접기전 길이가 홀수면 접은 후 소수점 이하 버리기 floor

13 * 17 30 * 15

가로 세로 크기 bill

'''
def solution(wallet, bill):
    answer = 0
    minWallet = min(wallet)
    maxWallet = max(wallet)
    minBill = min(bill)
    maxBill = max(bill)
    
    while (minBill > minWallet or maxBill > maxWallet):
        answer += 1
        if maxBill == bill[0]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        minBill = min(bill)
        maxBill = max(bill)
    
    return answer