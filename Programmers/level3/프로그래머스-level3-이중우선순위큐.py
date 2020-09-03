# -*- coding: utf-8 -*-
# 이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.
# 명령어	수신 탑(높이)
# I 숫자	큐에 주어진 숫자를 삽입합니다.
# D 1	큐에서 최댓값을 삭제합니다.
# D -1	큐에서 최솟값을 삭제합니다.
# 이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때,
# 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return
# 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제
# 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시

import heapq

def solution(operations):
    maxheap = []
    minheap = []

    # 최소힙, 최대힙 두가지 합을 만든다.
    # 추가할 때는 두 힙에 추가를 하고 최대값 삭제는 최대힙에서, 최솟값 삭제는 최소힙에서 삭제를 한다.
    # 값 추가와 삭제를 할 때 총 길이를 +1, -1 하면서 길이를 트래킹한다.
    # 길이가 0이 되면 두 힙을 모두 빈 힙으로 초기화하여 동기화 문제를 해결한다.
    leng = 0
    for el in operations:
        el = el.split(' ')
        # 삽입
        if el[0] == 'I':
            leng += 1
            heapq.heappush(minheap,int(el[1]))
            heapq.heappush(maxheap, (-int(el[1]),int(el[1])))
        else:
            # 최대값 삭제
            if el[1] == '1':
                if len(maxheap) != 0:
                    leng -= 1
                    heapq.heappop(maxheap)
            # 최솟값 삭제
            else:
                if len(minheap) != 0:
                    leng -= 1
                    heapq.heappop(minheap)
        if leng == 0:
            minheap = []
            maxheap = []

    left = 0
    right = 0
    if len(minheap) == 0 or len(maxheap) == 0:
        return [right,left]
    else:
        left = heapq.heappop(minheap)
        right = heapq.heappop(maxheap)[1]

    return [right,left]

operations = 	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))