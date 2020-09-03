# -*- coding: utf-8 -*-
# n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때,
# 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성
# 다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다.
# costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용
# 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.

def solution(n, costs):
    answer = 0

    # 섬을 연결하는 cost를 기준으로 오름차순으로 정렬한다.
    costs = sorted(costs, key = lambda x : x[2])

    network = [-1] * n
    count = 0

    # 서로 섬이 연결이 되어 있으면 연결된 섬들 중에서 숫자가 가장 작은 섬의 값을 network에 넣는다.
    # 같은 숫자면 서로 연결이 된 것이다.
    # 이미 연결이 되있는 섬은 건너뛰고 아니면 연결한다.
    # 모든 노드를 연결하는 수는 n-1이므로 n-1개 만큼 연결하면 while문은 나온다.
    while count != n -1:
        x = costs.pop(0)
        if network[x[0]] == -1 and network[x[1]] == -1:
            network[x[0]] = min(x[0],x[1])
            network[x[1]] = min(x[0],x[1])
            answer += x[2]
            count += 1
        elif network[x[0]] != network[x[1]]:
            if network[x[0]] == -1:
                network[x[0]] = network[x[1]]
            elif network[x[1]] == -1:
                network[x[1]] = network[x[0]]
            else:
                for i in range(0,len(network)):
                    if network[i] == max(network[x[0]],network[x[1]]) and i != x[0]  and i != x[1]:
                        network[i] = min(network[x[0]], network[x[1]])
                network[x[0]] = min(network[x[0]], network[x[1]])
                network[x[1]] = min(network[x[0]], network[x[1]])
            answer += x[2]
            count += 1

    return answer

n = 5
costs = [[0,1,1],[3,4,1],[1,2,2],[2,3,4]]
print(solution(n,costs))
