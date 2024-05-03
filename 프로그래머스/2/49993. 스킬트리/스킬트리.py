def solution(skill, skill_trees):
    answer = 0
    skills = {}
    for i, v in enumerate(list(skill)):
        skills[v] = i

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
        if pre == -2: # 선행 스킬을 수행 안한 경우
            continue
        else: # pre == -1 이면, 선행 스킬과 관련 없는 스킬트리
            answer += 1
    
    return answer
