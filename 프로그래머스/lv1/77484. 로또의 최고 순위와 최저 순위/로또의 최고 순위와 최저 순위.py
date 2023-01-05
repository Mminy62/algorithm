def solution(lottos, win_nums):
    # 갖고 있는 번호의 갯수를 센 후, 최고는 0의 갯수만큼 더해주고 최저는 아예 안더하면 된다.
    default = list(filter(lambda x : x in win_nums, lottos))
    result = [len(default) + lottos.count(0), len(default)]
    
    rank = map(lambda x: (7-x) if x > 1 else 6, result)
    
    return list(rank)