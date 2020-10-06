# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때,
# (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

from collections import deque

n,m = list(map(int,input().split()))

mirro = []
check = []

for _ in range(n):
    s = list(map(int,input()))
    mirro.append(s)
    temp = [0]*m
    check.append(temp)

def bfs():
    my_queue = deque([])
    my_queue.append([0,0])
    check[0][0] = 1
    count = 1

    while True:
        l = len(my_queue)
        end = 0
        for i in range(l):
            x,y = my_queue.popleft()
            if x == n-1 and y == m-1:
                end = 1
                break
            if x != n-1 and check[x+1][y] == 0 and mirro[x+1][y] == 1:
                check[x+1][y] = 1
                my_queue.append([x+1,y])
            if y != m-1 and check[x][y+1] == 0 and mirro[x][y+1] == 1:
                check[x][y+1] = 1
                my_queue.append([x,y+1])
            if x != 0 and check[x-1][y] == 0 and mirro[x-1][y] == 1:
                check[x-1][y] = 1
                my_queue.append([x-1,y])
            if y != 0 and check[x][y-1] == 0 and mirro[x][y-1] == 1:
                check[x][y-1] = 1
                my_queue.append([x,y-1])
        if end == 1:
            break
        count += 1

    return count

count = bfs()
print(count)

