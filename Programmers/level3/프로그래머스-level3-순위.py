# -*- coding: utf-8 -*-
# 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다.
# 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.
# 선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return
# [A, B]는 A 선수가 B 선수를 이겼다는 의미

def solution(n, results):
    answer = 0

    state = []
    for i in range(0,n+1):
        state.append([i,set([]),set([])])

    for el in results:
        win = el[0]
        lose = el[1]

        # 경기 결과가 하나 나올 때마다 이긴 선수와 이긴 선수를 이긴 선수들의 (승) 목록에 진 선수와 진선수에게 진 선수들을 넣는다.
        for el in state[lose][2]:
            state[el][1].add(win)
            for el2 in state[win][1]:
                state[el][1].add(el2)
            state[win][2].add(el)
        state[win][2].add(lose)

        # 위와 반대의 과정을 진행한다.
        for el in state[win][1]:
            state[el][2].add(lose)
            for el2 in state[lose][2]:
                state[el][2].add(el2)
            state[lose][1].add(el)
        state[lose][1].add(win)

    # 자신을 이긴 선수들과 자신에게 진 선수들의 합이 총 선수 -1 과 같으면 등수가 확정적이다.
    for i in range(1,len(state)):
        if len(state[i][1]) + len(state[i][2]) == n-1:
            answer += 1
    return answer

n = 5
results = [[2,5],[4, 3], [4, 2], [3, 2], [1, 2]]
n2 = 1
results2 = []
print(solution(n,results))