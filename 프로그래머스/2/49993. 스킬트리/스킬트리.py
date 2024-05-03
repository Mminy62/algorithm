def solution(skill, skill_trees):
    answer = 0
    skills = {}
    for i, v in enumerate(list(skill)):
        skills[v] = i
        
    # 스킬에 없는걸 다 배웠어도 가능

    for tree in skill_trees:
        pre = -1
        for c in list(tree):
            if c in skills.keys():
                if pre == skills[c] - 1:
                    pre = skills[c]
                    continue
                else:
                    pre = -2
                    break
        if pre == -2:
            continue
        else:
            answer += 1

                    
    return answer
'''
선행 스킬 순서에 맞는 스킬 트리를 찾는 것
선행 스킬에 첫번째 단어가 아니면, 무조건 앞에 단어들도 포함되어야함
dict로 해서 0이 아니면, 앞에 단어들이 있는지 확인 해야함
pre를 통해서 앞에 단어 확인 -1인지 
'''