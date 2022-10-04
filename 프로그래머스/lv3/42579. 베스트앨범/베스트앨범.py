def solution(genres, plays):
    answer = []
    
    music_play = {}
    
    music_dict = {}
    
    for k,v in zip(genres,plays):
        music_play[k]=music_play.get(k,0)+v
        
    
    for k,v,i in zip(genres,plays,range(len(plays))):
        if k not in music_dict.keys():
            music_dict[k] = [(i,v)]
        else:
            music_dict[k].append((i,v))
            
    for i in range(len(music_dict.keys())):
        max_genre = max(music_play,key=music_play.get) #play 수의 최대값 장르 구하기
        music_play.pop(max_genre)
        
        num_plays = music_dict.pop(max_genre)
        sorted_dict = sorted(num_plays, key = lambda item: item[1], reverse = True)
        
        if len(sorted_dict) > 1:
            answer.append(sorted_dict[0][0])
            answer.append(sorted_dict[1][0])
        else:
            answer.append(sorted_dict[0][0])
        

    return answer