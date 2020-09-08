# -*- coding: utf-8 -*-
# 셔틀은 09:00부터 총 n회 t분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 m명의 승객이 탈 수 있다.
# 셔틀은 도착했을 때 도착한 순간에 대기열에 선 크루까지 포함해서 대기 순서대로 태우고 바로 출발한다.
# 예를 들어 09:00에 도착한 셔틀은 자리가 있다면 09:00에 줄을 선 크루도 탈 수 있다.
# 콘이 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각을 구하여라.
# 단, 콘은 게으르기 때문에 같은 시각에 도착한 크루 중 대기열에서 제일 뒤에 선다.
# 또한, 모든 크루는 잠을 자야 하므로 23:59에 집에 돌아간다. 따라서 어떤 크루도 다음날 셔틀을 타는 일은 없다.
# 셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한 셔틀에 탈 수 있는 최대 크루 수 m

from collections import deque

def solution(n, t, m, timetable):
    answer = ''

    bus = []
    bus.append(540)
    for i in range(n-1):
        bus.append(540+((i+1)*t))

    line = 0
    people = []
    for el in timetable:
        temp = list(map(int,el.split(':')))
        people.append(temp[0]*60 + temp[1])
        if temp[0]*60 + temp[1] <= 540: line += 1
    people.sort()
    people = deque(people)

    last = bus[-1]

    for i in range(len(bus)):
        if bus[i] != last:
            for j in range(m):
                if people[0] <= bus[i]:
                    people.popleft()
        else:
            for p in range(len(people)):
                if people[p] > bus[i]:
                    index = p
                    break
            else:
                index = len(people)
            if index < m:
                answer = last
            else:
                x = people[m-1]
                answer = x-1

    answer = [str(answer//60),str(answer%60)]
    if len(answer[0]) == 1: answer[0] = '0'+answer[0]
    if len(answer[1]) == 1: answer[1] = '0'+answer[1]
    return answer[0]+':'+answer[1]

n = 10
t = 60
m = 45
timetable = ['23:59','23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59']
print(solution(n,t,m,timetable))