# -*- coding: utf-8 -*-
# 예를 들어 튜플이 (2, 1, 3, 4)인 경우 이는
# {{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
# 순서는 상관 없이 주어진다. 중괄호 안에 숫자들도 순서가 없다. 튜플은 중복이 없다.
# 튜플의 집합이 주어질 때 튜플을 구하라
# 단, 튜플은 순서가 있다.

def solution(s):
    # 스트링을 리스트 형태로 바꿔주기
    s = s[2:-2]
    s = s.split('},{')
    for i in range(0,len(s)):
        s[i] = s[i].split(',')

    answer = []
    index = 0

    # 개수가 하나인 것이 제일 앞 개수가 두 개인 것 중에 하나가 그 다음
    # 이 순서를 이용해서 하나씩 추가
    while len(s) != len(answer):
        for el in s:
            if len(el) == index+1:
                for e in answer:
                    el.remove(e)
                answer += el
                index += 1
    for i in range(0,len(answer)):
        answer[i] = int(answer[i])
    return answer

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))