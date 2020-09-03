# -*- coding: utf-8 -*-
# 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다.
# 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다

def solution(triangle):

    # 위에서 부터 내려오면서 각층에서의 각 값에 대해 가질 수 있는 최대의 값을 채워 넣는다.
    # dp 알고리즘 사용 
    for i in range(1,len(triangle)):
        for j in range(0,len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])

    return max(triangle[-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))