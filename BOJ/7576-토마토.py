# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

import sys
from collections import deque
x,y = list(map(int,sys.stdin.readline().split()))

num = 0
tomato = []
count = 0
bad = deque([])


for i in range(y):
    temp = list(map(int,sys.stdin.readline().split(' ')))
    for j in range(len(temp)):
        if temp[j] == 0:
            num += 1
        if temp[j] == 1:
            bad.append([i,j])
    tomato.append(temp)

while len(bad) != 0:

    l = len(bad)
    for i in range(l):
        p,q = bad.popleft()
        if tomato[max(0,p-1)][q] == 0:
            bad.append([max(0,p-1),q])
            tomato[max(0, p - 1)][q] = 1
            num -= 1
        if tomato[p][max(0,q-1)] == 0:
            bad.append([p,max(0,q-1)])
            tomato[p][max(0, q - 1)] = 1
            num -= 1
        if tomato[min(y-1,p+1)][q] == 0:
            bad.append([min(y-1,p+1),q])
            tomato[min(y - 1, p + 1)][q] = 1
            num -= 1
        if tomato[p][min(x-1,q+1)] == 0:
            bad.append([p,min(x-1,q+1)])
            tomato[p][min(x - 1, q + 1)] = 1
            num -= 1

    count += 1

if num != 0: print(-1)
else: print(count-1)