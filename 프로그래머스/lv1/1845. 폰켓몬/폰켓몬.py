def solution(nums):
    answer = 0
    
    N = len(nums)//2 
    
    typeNum = len(set(nums))
    
    if typeNum > N:
        return N
    else: # N <= typeNum
        return typeNum
    
    '''
    N/2 가져가도 됨
    최대한 다양한 종류의 n/2를 가지는 방법 -> 종류의 수 return
    set으로 중복 제거 하고 몇마리 뽑는지 알고 
    N/2가 set보다 크면 set수
    set이 N/2보다 크면 N/2 리턴
    
    
    '''
    return answer