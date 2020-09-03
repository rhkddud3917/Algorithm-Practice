# -*- coding: utf-8 -*-
# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return
# 서로 연결이 되어있으면 하나의 네트워크
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현

global network

# dfs 를 통해 각 노드의 값이 자신이 연결되어 있는 최소 값의 노드를 가지고 있도록 하였다.
def dfs(computers,i,val):

    global network
    for j in range(0,len(computers[i])):
        if computers[i][j] == 1:
            if network[j] == -1:
                network[j] = val
                dfs(computers,j,val)
    return


def solution(n, computers):

    global network

    network = [-1] * n
    for i in range(0,len(computers)):
        dfs(computers,i,i)

    return len(set(network))

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,computers))