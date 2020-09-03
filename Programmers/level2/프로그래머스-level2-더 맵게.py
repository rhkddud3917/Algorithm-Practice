# -*- coding: utf-8 -*-
# 스코빌 지수가 낮은 것을 섞어 스코빌 지수를 높인다.
# 원하는 수치 만큼 높아야 한다. 섞는 횟수 반환
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) == 1:
            if scoville[0] < K:
                return -1
            else:
                return answer
        x = heapq.heappop(scoville)
        if x >= K:
            return answer
        y = heapq.heappop(scoville)
        z = x + y*2
        heapq.heappush(scoville,z)
        answer += 1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville,K))