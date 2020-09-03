# -*- coding: utf-8 -*-
# 스킬은 배우기 위해서는 선행 스킬을 배워야함
# 선행 스킬목록에 없는 스킬들은 언제든지 배울 수 있음
# 선행 스킬 목록을 보고 가능한 스킬트리의 개수를 출력

def solution(skill, skill_trees):
    skill = list(skill)
    fail = 0
    answer = 0
    for el in skill_trees:
        count = 0
        s_tree = list(el)
        for el2 in s_tree:
            if el2 in skill:
                if count < skill.index(el2):
                    fail = 1
                else:
                    count += 1
            if fail == 1:
                break
        if fail == 1:
            fail = 0
            continue
        else:
            answer += 1

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))