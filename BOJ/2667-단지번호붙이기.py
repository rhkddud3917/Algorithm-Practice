# -*- coding: utf-8 -*-
# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 대각선말고 상하좌우 붙어있는 그룹을 단지라고 한다.
# 단지에 속하는 아파트수를 오름차순으로 출력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

n = int(input())
home = []
check = []
for i in range(n):
    temp = list(input())
    home.append(temp)
    check.append([0]*n)

# 연결된 집들을 연결의 끝까지 dfs를 통해 접근을 해서 해당 단지를 입력한다.
def dfs(i,j):
    m1 = max(0,i-1)
    M1 = min(n-1,i+1)
    m2 = max(0,j-1)
    M2 = min(n-1,j+1)

    # 단지의 말단부분에 도달하면 return을 한다.
    if (home[M1][j] == '0' or check[M1][j] != 0) and \
        (home[m1][j] == '0' or check[m1][j] != 0) and \
        (home[i][M2] == '0' or check[i][M2] != 0) and \
        (home[i][m2] == '0' or check[i][m2] != 0):
        return

    # 단지의 말단 부분까지 dfs를 통해 접근한다.
    if i != 0 and home[i-1][j] == '1' and check[i-1][j] == 0:
        check[i-1][j] = check[i][j]
        homes[count-1] += 1
        dfs(i-1,j)
    if i != n-1 and home[i+1][j] == '1' and check[i+1][j] == 0:
        check[i+1][j] = check[i][j]
        homes[count - 1] += 1
        dfs(i+1,j)
    if j != 0 and home[i][j-1] == '1' and check[i][j-1] == 0:
        check[i][j-1] = check[i][j]
        homes[count - 1] += 1
        dfs(i,j-1)
    if j != n-1 and home[i][j+1] == '1' and check[i][j+1] == 0:
        check[i][j+1] = check[i][j]
        homes[count - 1] += 1
        dfs(i,j+1)

    return


count = 1
homes = [0]
for i in range(n):
    for j in range(n):
        if home[i][j] == '1':
            if check[i][j] == 0:
                check[i][j] = count
                count += 1
                homes.append(1)
                dfs(i,j)

print(count-1)
homes.sort()
for i in range(1,len(homes)):
    print(homes[i])



