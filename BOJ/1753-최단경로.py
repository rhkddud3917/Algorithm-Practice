# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성

from heapq import heappop,heappush
import sys

inf = 100000000
v,e = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())

dict = []
for _ in range(v+1):
    dict.append([])
main = []
dis = [inf]*(v+1)

def dijkstra(start):
    heappush(main, [0, start])
    dis[start] = 0
    while main:
        x,y = heappop(main)
        for a,b in dict[y]:
            tmp = dis[y] + b
            if dis[a] > tmp:
                heappush(main,[tmp,a])
                dis[a] = tmp

for i in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    dict[a].append([b,c])

dijkstra(start)

for i in dis[1:]:
    if i == inf: print("INF")
    else: print(i)

