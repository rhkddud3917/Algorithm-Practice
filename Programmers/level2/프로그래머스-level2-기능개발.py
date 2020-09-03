# -*- coding: utf-8 -*-
# progresses는 현재 하고 있는 일이 진행된 퍼센트를 나타낸 것
# sppeds는 하루에 얼만큼의 퍼센트를 진행할 수 있는지
# 앞의 작업이 완료되기 전에 뒤의 작업이 배포될 수 없다. 대신에 미리 작업이 완료될 수는 있다.
# 순서대로 배포되는 작업의 수를 출력

def solution(progresses, speeds):
    endList = []
    answer = []
    for el in progresses:
        endList.append([0,el])
        idx = 0
    for i in range(1,101):
        if idx == len(endList):
            break
        answer_count = 0
        for el in range(0,len(endList)):
            endList[el][1] = endList[el][1] + speeds[el]
            if endList[el][1] >= 100:
                endList[el][0] = 1
        while endList[idx][0] == 1:
            answer_count += 1
            idx += 1
            if idx == len(endList):
                break
        if answer_count != 0:
            answer.append(answer_count)
            answer_count = 0
    return answer

progress = [93,30,55]
speeds = [1,30,5]
print(solution(progress, speeds))