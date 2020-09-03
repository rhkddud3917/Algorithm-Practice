# -*- coding: utf-8 -*-
# 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다.
# 퇴근 까지 남은 n 시간 동안 작업을 수행하여 야근 피로도를 최소화하려한다.
# 야근 피로도의 최솟값 리턴

import heapq

def solution(n, works):
    answer = 0

    # 현재 작업량을 최대값을 우선순위로 하는 heap에 저장한다.
    work_heap = []
    for el in works:
        heapq.heappush(work_heap,(-el,el))

    # 남은 n 시간 동안 작업량이 최대인 것을 뽑아 작업을 진행한다.
    # 이렇게 해야 제곱의 합이 최소가 된다.
    for i in range(0,n):
        x = heapq.heappop(work_heap)
        x = x[1] -1
        if x < 0:
            return 0
        heapq.heappush(work_heap,(-x,x))

    for el in work_heap:
        answer += el[1]**2
    return answer

n = 4
works = [4, 3, 3]
print(solution(n,works))