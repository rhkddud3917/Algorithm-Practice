# -*- coding: utf-8 -*-
# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.
# 문서의 중요도와 내가 인쇄하고 싶어하는 문서의 location이 주어질 때 언제 내 문서가 인쇄될지 출력

def solution(priorities, location):
    answer = 1
    while priorities != []:
        x = priorities[0]
        fail = 0
        for i in range(1,len(priorities)):
            if x < priorities[i]:
                fail = 1
                break
        if fail == 1:
            x = priorities.pop(0)
            priorities.append(x)
            if location == 0:
                location = len(priorities) -1
            else:
                location -= 1
        else:
            if location == 0:
                return answer
            else:
                del priorities[0]
                location -= 1
                answer += 1

    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities,location))