# -*- coding: utf-8 -*-
# 한번에 최대 2명까지 태울 수 있다. 무게 제한이 있다.
# 모든 사람을 구하는 구명보트 개수 반환하기
# 사람을 못구하는 경우는 없다.

from collections import deque

def solution(people, limit):
    answer = 0

    # O(nlogn)
    people.sort()
    people = deque(people)

    # 사람을 무게 순대로 정렬을 하여
    # 먼저 무거운 사람 순대로 최대한 채우고
    # 그 후 가벼운 사람들을 순서대로 채운다.
    # 그렇게 꽉 차면 보트 개수를 하나 증가시킨다.
    while len(people) != 0:
        weight = 0
        # 무거운 순으로 추가
        while weight <= limit:
            if len(people) == 0: break
            x = people[len(people)-1]
            if weight + x > limit: break
            else:
                weight += people.pop()
        # 가벼운 순으로 추가
        while weight <= limit:
            if len(people) == 0: break
            x = people[0]
            if weight + x > limit: break
            else:
                weight += people.popleft()
        answer += 1
    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people,limit))