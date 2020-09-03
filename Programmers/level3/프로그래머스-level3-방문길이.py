# -*- coding: utf-8 -*-

def solution(dirs):
    # 현재 좌표
    cur = [0, 0]
    # 다음 좌표
    next = [0, 0]
    # 경로
    load = []
    # 스트링 분리
    dirs = list(dirs)

    for el in dirs:
        # deep copy
        cur[0] = next[0]
        cur[1] = next[1]
        if (el == "U"):
            if (cur[1] == 5):
                continue
            else:
                next[1] = cur[1] + 1
        elif (el == "D"):
            if (cur[1] == -5):
                continue
            else:
                next[1] = cur[1] - 1
        elif (el == "L"):
            if (cur[0] == -5):
                continue
            else:
                next[0] = cur[0] - 1
        elif (el == "R"):
            if (cur[0] == 5):
                continue
            else:
                next[0] = cur[0] + 1

        # 경로에 추가
        if ([cur[0], cur[1], next[0], next[1]] in load or [next[0], next[1], cur[0], cur[1]] in load):
            continue
        else:
            load.append([cur[0], cur[1], next[0], next[1]])

    answer = len(load)
    return answer