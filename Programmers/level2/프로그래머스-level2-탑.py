# -*- coding: utf-8 -*-
# 신호는 왼쪽으로 송신을 한다
# 송신한 탑 보다 높은 탑이 수신을 할 수 있다.
# 한 번 수신되면 신호는 더 가지 않는다.
# 수신되지 않으면 0으로 출력
# 각 인덱스별로 송신한 신호를 수신한 탑의 인덱스를 출력해라 1로 시작

def solution(heights):
    answer = []
    heights.reverse()

    while True:
        if heights == []: break
        x = heights.pop(0)
        flag = 0
        for el in range(0,len(heights)):
            if x < heights[el]:
                answer.append(el)
                flag = 1
                break
        if flag == 0:
            answer.append(-1)

    res = []
    answer.reverse()
    for el in range(0,len(answer)):
        if answer[el] == -1:
            res.append(0)
        else:
            res.append(el-answer[el])
    return res

heights = [3,9,9,3,5,7,2]
print(solution(heights))