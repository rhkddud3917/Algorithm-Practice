# -*- coding: utf-8 -*-
# 1번 마을에서 배달을 하려고 하는데
# N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다.
# 음식 주문을 받을 수 있는 마을의 개수를 return

import heapq

# 다익스트라 알고리즘을 사용했다.
def solution(N, road, K):
    answer = 0
    n, k = N, K

    dis = [0]+[1000000000]*(n-1)

    road.sort()
    road_dict = {}

    # 방향이 없는 간선이므로
    # 딕셔너리에 양 방향을 모두 추가
    for el in road:
        try:
            road_dict[el[0]-1].append([el[1]-1,el[2]])
        except:
            road_dict[el[0]-1] = [[el[1]-1,el[2]]]
        try:
            road_dict[el[1]-1].append([el[0]-1, el[2]])
        except:
            road_dict[el[1]-1] = [[el[0]-1, el[2]]]

    # 힙에 출발지를 넣음
    # (출발지와의 거리, 인덱스)
    que = []
    heapq.heappush(que,(dis[0],0))

    # 힙에서 팝을 한다.
    # 팝 한 노드를 중심으로 연결되어 잇는 노드의 현재 출발지와의 거리가
    # 출발지로부터 팝을 한 노드까지의 거리와 두 노드까지의 거리의 합보다 크면
    # 연결되어 있는 노드의 출발지와의 거리를 업데이트하고
    # 힙에 푸시한다.
    while que:
        x = heapq.heappop(que)
        if x[1] in road_dict.keys():
            for el in road_dict[x[1]]:
                if dis[el[0]] > dis[x[1]]+el[1]:
                    dis[el[0]] = dis[x[1]]+el[1]
                    heapq.heappush(que,(dis[x[1]]+el[1],el[0]))

    for el in dis:
        if el <= k: answer += 1


    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N,road,K))