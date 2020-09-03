# -*- coding: utf-8 -*-
# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
# x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
# 구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제합니다.
# 설치 또는 삭제를 한 후에
# 조건을 만족하지 않게 되면 해당 작업은 무시된다.
# return 하는 배열은 x [x,y,a] 좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
# x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.

def check(x,y,a,b,result):
    # 설치하기 위한 조건을 확인하고 조건이 맞으면 설치 아니면 무시
    if b == 1:
        # 기둥 설치 판단
        if a == 0:
            if y == 0:
                result.append([x,y,a])
                return result
            if [x,y-1,0] in result:
                result.append([x,y,a])
                return result
            if [x-1,y,1] in result:
                result.append([x, y, a])
                return result
            if [x,y,1] in result:
                result.append([x, y, a])
                return result
            return result
        # 보 설치 판단
        elif a == 1:
            if [x,y-1,0] in result or [x+1,y-1,0] in result or ([x-1,y,1] in result and [x+1,y,1] in result):
                result.append([x,y,a])
                return result
            return result
    # 삭제하고 난 후에도 조건들이 만족하는지 확인을 하고 만족하면 삭제 아니면 무시
    elif b == 0:
        # 기둥의 삭제 판단
        if a == 0:
            if [x,y+1,0] in result:
                if ([x,y+1,1] not in result and [x-1,y+1,1] not in result):
                    return result
            if [x,y+1,1] in result:
                if ([x+1,y,0] not in result and ([x-1,y+1,1] not in result or [x+1,y+1,1] not in result)):
                    return result
            if [x-1,y+1,1] in result:
                if ([x-1,y,0] not in result and ([x,y+1,1] not in result or [x-2,y+1,1] not in result)):
                    return result
            result.remove([x, y, a])
            return result
        # 보의 삭제 판단
        elif a == 1:
            if [x,y,0] in result:
                if ([x,y-1,0] not in result and [x-1,y,1] not in result):
                    return result
            if [x+1,y,0] in result:
                if ([x+1,y-1,0] not in result and [x+1,y,1] not in result):
                    return result
            if [x-1,y,1] in result:
                if ([x-1,y-1,0] not in result and [x,y-1,0] not in result):
                    return result
            if [x+1,y,1] in result:
                if ([x+1,y-1,0] not in result and [x+2,y-1,0] not in result):
                    return result
            result.remove([x,y,a])
            return result
        return result

def solution(n, build_frame):
    result = []

    for el in build_frame:
        x = el[0]
        y = el[1]
        a = el[2]
        b = el[3]
        if b == 1:
            if a == 0:
                if x < 0 or x > n or y >= n or y < 0: continue
            if a == 1:
                if x < 0 or x >= n or y > n or y < 0: continue
        result = check(x,y,a,b,result)

    result = sorted(result,key=lambda x: (x[0],x[1],x[2]))
    return result

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n,build_frame))