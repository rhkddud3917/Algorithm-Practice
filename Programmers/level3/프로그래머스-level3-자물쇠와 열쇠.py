# -*- coding: utf-8 -*-
# 열쇠는 회전과 이동이 가능하다.
# 자물쇠의 홈 부분을 모두 채울 수 있어야 열 수 있다.
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만,
# 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다.
# 열쇠가 자물쇠에 완전히 포개어질 필요는 없다.

import copy

# 키를 90도 만큼 돌려주는 함수
def lotate(x):
    res = []
    for i in range(0,len(x)):
        tmp = []
        for j in range(0,len(x)):
            tmp.append(0)
        res.append(tmp)

    for i in range(0,len(x)):
        for j in range(0,len(x)):
            res[len(x)-1-i][len(x)-1-j] = x[j][len(x)-1-i]
    return res

def solution(key, lock):

    count = 0
    while True:
        # 키를 90도씩 총 3번 돌릴 수 있으므로 카운트로 방향에 대한 경우의 수를 셈
        if count == 4: break
        for i in range(-len(key)+1,len(lock)):
            for j in range(-len(key)+1,len(lock)):
                # 키가 자물쇠와 완전히 겹쳐지지 않을 수도 있으므로
                # 겹쳐지는 부분에 대해 iterate 할 범위를 구하는 과정
                tmp = copy.deepcopy(lock)
                li = max(0,-i)
                ri = min(len(key),len(lock)-i)
                lj = max(0,-j)
                rj = min(len(key),len(lock)-j)
                fail = 0
                # 키와 자물쇠를 맞추어 보는 과정에서
                # 돌기와 돌기가 만날때 즉 합이 2가 되면 실패이므로 continue 하고
                # 아니면 키와 자물쇠의 값을 더한다.
                for x in range(li,ri):
                    for y in range(lj,rj):
                        if tmp[x+i][y+j] + key[x][y] == 2:
                            fail = 1
                            break
                        else: tmp[x+i][y+j] += key[x][y]
                    if fail == 1: break
                if fail == 1: continue
                # 둘이 포갰을 때 0이 있으면 안됨
                # lock의 홈이 모두 채워지면 True 리턴
                no = 0
                for el in tmp:
                    for el2 in el:
                        if el2 == 0:
                            no = 1
                            break
                    if no == 1: break
                if no == 0: return True
        count += 1
        key = lotate(key)

    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))

