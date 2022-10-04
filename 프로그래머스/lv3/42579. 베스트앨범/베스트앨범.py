def solution(genres, plays):
    answer = []
    music_play=dict()

    # 장르별로 play 횟수
    for k,v in zip(genres,plays):
        music_play[k]=music_play.get(k,0)+int(v)

    # play 횟수 내림차순으로 정렬
    play_list=sorted(music_play.items(), key=lambda x:x[1], reverse=True)

    # 많이 재생된 장르 순으로 for문 돌리기
    for l, cnt in play_list:
        arr=[]
        # 재생횟수와 고유번호 넣어주기
        for idx,(g, p) in enumerate(zip(genres,plays)):
            if g==l:
                arr.append([p,idx])

        # 조건 2,3 을 고려한 정렬
        arr=sorted(arr,key = lambda x : (x[0],-x[1]),reverse=True)

        for i in range(min(len(arr),2)):
            answer.append(arr[i][1])

    return answer
# def get_largest(playDict):
    
#     result = []
#     #고유번호: 재생수 의 dictionary 에서 value를 기준으로 정렬
#     print(playDict.items())
#     sorted_dict = sorted(playDict.items(), key = lambda item: item[1], reverse = True) #sorted items를 key라는 람다 함수로 만드는 것
    
        
#     if len(sorted_dict) > 1:
#         result.append(sorted_dict[0][0])
#         result.append(sorted_dict[1][0])
#     else:
#         result.append(sorted_dict[0][0])
    
    
#     return result

# def solution(genres, plays):
#     answer = []
    
#     playDict = {}
#     '''
#     playDict = {
#         "classic" :{
#                 0: 500,
#                 2: 150,
#                 3: 800
#         },
#         "pop" : {
#                 1: 600,
#                 4: 2500
#         }
#     }
#     '''
    
#     for k, v, n in zip(genres,plays, range(len(plays))):
#         if k not in playDict.keys():
#             playDict[k] = {n: v}
#         else:
#             playDict.get(k).update({n:v})

#     temp = [] #합만 모은 list, max의 index 구하고 pop
    
#     for dictData in playDict.values():
#         temp.append(sum(dictData.values()))
    
#     for i in range(len(playDict)):
#         index = temp.index(max(temp))
#         temp.pop(index)
#         key = list(playDict)[index]
#         result = get_largest(playDict[key])
        
#         for data in result:
#             answer.append(data)
        
        

#     return answer
