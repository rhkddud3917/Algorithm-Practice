# -*- coding: utf-8 -*-
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 'ICN' 공항에서 출발
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.

# 모든 티켓을 소비하기 위한 dfs
# 모든 티켓을 소비하기 전까지 dfs를 한다.
def dfs(root,start,count,res):

    if count == len(root):
        return res

    for i in range(0,len(root)):
        if root[i][0][0] == start:
            if root[i][1] == 0:
                root[i][1] = 1
                res.append([start,root[i][0][1]])
                count += 1
                x = dfs(root,root[i][0][1],count,res)
                if len(x) != 0: return x
                count -= 1
                root[i][1] = 0
                res.pop(-1)

    return []

def solution(tickets):


    res = []
    count = 0

    # 모든 조건을 만족할 때 알파벳 순으로 나열된 것 중 가장 빠른 것을 반환해야 하므로
    # 미리 알파벳 순으로 sort를 해 놓는다.
    root = sorted(tickets, key = lambda x: (x[0],x[1]))
    for i in range(0,len(root)):
        root[i] = [root[i],0]

    res.append(['ICN','ICN'])
    answer = dfs(root,'ICN',count,res)

    ret = []
    for el in answer:
        ret.append(el[1])

    return ret

tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
tickets2 = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
tickets3 = [['ICN','A'],['ICN','B'],['B','ICN']]
tickets4 = [['ICN','A'],['A','B'],['B','A'],['A','ICN'],['ICN','A']]
print(solution(tickets4))