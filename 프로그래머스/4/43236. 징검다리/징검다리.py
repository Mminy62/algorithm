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
        else:
            min_value = mid
            start = mid + 1

                
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


 # if removecnt == n:
            #     min_value = mid 
            ## 이 부분에서 막혔다. n개를 반드시 지운상태에서의 거리의 최소값을 생각했는데 이 조건을 안걸면 removecnt <= n인 mid값은 다 저장하니,, n개를 반드시 지울필요가 없는데 그런 얘기는 지문에 없기 때문이다. 
            # n개를 제거한 뒤라며!!!!!
            
      ₩₩₩      
덕분에 답을 알았네요. 저도 계속 두 개 정도 틀려서 뭐가 잘못됐나 했는데 덕분에 풀었습니다.

아래 예로 테스트 해 보세요.

input: [23, [3, 6, 9, 10, 14, 17], 2]
output: 3
이 경우 mid 값에 따른 지워야할 바위의 갯수는 아래와 같습니다.

mid	1	2	3	4	5
rock_cnt	0	1	1	3	4
rock_cnt 값이 2가 되는 경우는 있을 수 없으므로 아마 answer 0이 될 것입니다.
하지말 실제로 답은 3이되어야 겠죠. 즉 2개를 없애면 1개를 없앨 때와 마찬가지로 최소거리가 3이 되도록 만들 수 있습니다.
'''