# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데,
# 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
# 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

import sys

s = sys.stdin.readline().rstrip().split(' ')
r,c = int(s[0]), int(s[1])

data = []
for i in range(0,r):
    row = list(map(lambda x: ord(x)-65,sys.stdin.readline().rstrip()))
    data.append(row)

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_dict = {}
for i in range(0,len(s)):
    alpha_dict[ord(s[i])-65] = 0


answer = 0
dist = 1
i ,j = 0, 0
alpha_dict[data[0][0]] = 1
passed = [data[0][0]]

def dfs(i, j,dist):
    global answer
    global data
    global alpha_dict

    if answer < dist: answer = dist
    # 위쪽
    if i > 0:
        if alpha_dict[data[i-1][j]] == 0:
            alpha_dict[data[i-1][j]] += 1
            dfs(i-1,j,dist+1)
            alpha_dict[data[i - 1][j]] -= 1
    # 오른쪽
    if j < c-1:
        if alpha_dict[data[i][j+1]] == 0:
            alpha_dict[data[i][j+1]] += 1
            dfs(i,j+1,dist+1)
            alpha_dict[data[i][j + 1]] -= 1
    # 아래쪽
    if i < r-1:
        if alpha_dict[data[i+1][j]] == 0:
            alpha_dict[data[i+1][j]] += 1
            dfs(i+1,j,dist+1)
            alpha_dict[data[i + 1][j]] -= 1
    # 왼쪽
    if j > 0:
        if alpha_dict[data[i][j-1]] == 0:
            alpha_dict[data[i][j-1]] += 1
            dfs(i,j-1,dist+1)
            alpha_dict[data[i][j - 1]] -= 1

    return

dfs(i,j,1)
print(answer)





