# -*- coding: utf-8 -*-
# 고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면
# 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.
# routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점,
# routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
# 차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.

def solution(routes):

    cam = []
    routes.sort()

    # 카메라가 존재할 수 있는 구간을 업데이트 한다. 최대한 많은 차량을 포함할 수 있도록
    # 카메라의 구간과 차량의 구간이 겹칠 경우 겹치는 구간을 카메라의 구간으로 바꾼다.
    # 겹치지 않는 경우 새로운 카메라가 필요한 것이므로 차량의 구간을 새로운 카메라의 구간으로 추가한다.
    # cam 리스트의 크기가 카메라의 최소 개수이다.
    for el in routes:
        if cam == []:
            cam.append(el)
        else:
            good = 0
            for c in range(0,len(cam)):
                if cam[c][1] < el[0] or cam[c][0] > el[1]:
                    continue
                else:
                    cam[c][0] = max(cam[c][0],el[0])
                    cam[c][1] = min(cam[c][1],el[1])
                    good = 1
                    break
            if good == 0:
                cam.append(el)

    return len(cam)

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))