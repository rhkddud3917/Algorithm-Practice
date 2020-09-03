# -*- coding: utf-8 -*-
# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때,
# 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

from collections import deque
import copy

# bfs 알고리즘을 통해 노드 1로 부터 각 노드 사이의 최단 거리를 구한다.
def bfs(edge,n):
    myqueue = deque([])
    check_dict = {}
    check = [0] * (n+1)
    for i in range(1,n+1):
        check_dict[i] = []
    for el in edge:
        check_dict[el[0]].append(el[1])
    myqueue.appendleft(1)
    check[1] = -1
    count = 1

    while len(myqueue) != 0:
        l = len(myqueue)
        for i in range(0,l):
            x = myqueue.pop()
            for el in check_dict[x]:
                if check[el] == 0:
                    myqueue.appendleft(el)
                    check[el] = count
        count += 1

    return check

def solution(n, edge):

    # bfs 를 하기 위해 노드 간의 간선을 추가한다.
    # 간선의 방향이 없으므로 각 노드에 대해서 추가한다.
    new_edge = []
    for i in range(0,len(edge)):
        new_edge.append(copy.deepcopy(edge[i]))
        edge[i].reverse()
        new_edge.append(edge[i])
    new_edge.sort()
    check = copy.deepcopy(bfs(new_edge,n))
    check = check[1:]
    check.sort(reverse=True)
    ans = 0
    for i in range(1,len(check)):
        if check[i] != check[i-1]:
            ans = i
            break
    return ans

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,edge))