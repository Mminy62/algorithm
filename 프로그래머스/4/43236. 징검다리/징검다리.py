def solution(distance, rocks, n): 
    rocks.sort()
    start = 0
    end = distance
    min_value = 1e9
    
    while start <= end:
        prev = 0
        removecnt = 0
        mid = (start + end) // 2
        
        # 순회하면서 갯수 세기
        for rock in rocks+[distance]:# 목적지 포함
            if rock - prev < mid:
                removecnt += 1
                if removecnt > n: break
                
            else: # 차이가 mid보다 크거나 같다->정상
                prev = rock
                
        if removecnt > n:# 조건에 맞는 mid가 아닌거야
            end = mid - 1
        else: # 조건에 맞는데 더 큰 값이 있을 수 있다 (거리의 최솟값 중에 가장 큰 값을 return)
            # if removecnt == n:
            #     min_value = min(min_value, mid)
            start = mid + 1
            min_value = mid # 최대값을 포함하므로

                
    return min_value


'''
1:15~35 20분
출발 0 도착 distance 
바위위치 
제거할 바위의 수 n이 매개변수
거리의 최소값 중 가장 큰 값 return 

순차적으로 돌면서 다 뺄수 X

--> 이번에도 조건 생각을 못했다. 
이분탐색 조건 다 외우자(적어놓기)
'''