# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
# 맵의 크기와 사과의 개수, 사과의 크기 뱀의 움직임이 주어진다.
# 방향 전환은 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻
# 방향 전환이 없으면 앞으로 이동

from collections import deque

n = int(input())
apple = int(input())

board = []
for _ in range(n):
    board.append([0]*n)

for i in range(apple):
    x,y = map(int,input().split())
    board[x-1][y-1] = 1

move = int(input())
go = {}
for i in range(move):
    s = list(input().split(' '))
    go[int(s[0])] = s[1]

snake = deque([[0,0]])

time = 0
head = 0 # 0 1 2 3 r d l u
while True:
    time += 1

    if head == 0:
        p = snake[-1][0]
        q = snake[-1][1]+1
        if q == n or [p,q] in snake: break
        snake.append([p,q])
        if board[p][q] == 0:
            snake.popleft()
        else:
            board[p][q] = 0

    elif head == 1:
        p = snake[-1][0]+1
        q = snake[-1][1]
        if p == n or [p, q] in snake: break
        snake.append([p, q])
        if board[p][q] == 0:
            snake.popleft()
        else:
            board[p][q] = 0

    elif head == 2:
        p = snake[-1][0]
        q = snake[-1][1]-1
        if q == -1 or [p, q] in snake: break
        snake.append([p, q])
        if board[p][q] == 0:
            snake.popleft()
        else:
            board[p][q] = 0

    elif head == 3:
        p = snake[-1][0]-1
        q = snake[-1][1]
        if p == -1 or [p, q] in snake: break
        snake.append([p, q])
        if board[p][q] == 0:
            snake.popleft()
        else:
            board[p][q] = 0

    try:
        x = go[time]
    except:
        x = ''
    if x != '':
        if head == 0:
            if x == 'L': head = 3
            elif x == 'D': head = 1
        elif head == 1:
            if x == 'L': head = 0
            elif x == 'D': head = 2
        elif head == 2:
            if x == 'L': head = 1
            elif x == 'D': head = 3
        elif head == 3:
            if x == 'L': head = 2
            elif x == 'D': head = 0

print(time)