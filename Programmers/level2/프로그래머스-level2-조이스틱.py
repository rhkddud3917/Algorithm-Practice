# -*- coding: utf-8 -*-
# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동
# 조이스틱을 이용해 단어를 만드는 최소 조작 횟수를 반환
# 맨 처음엔 A로만 이루어져 있음

# 가장 긴 A 문자열을 찾는다.
def find_empty(name):
    max = 0
    count = 0
    start = 0
    end = 0
    for el in range(0,len(name)):
        if name[el] == 1:
            count += 1
        else:
            if max < count:
                max = count
                count = 0
                end = el-1
                start = end - max +1

    return [start, end, max]

# A에서 알파벳을 만드는 조이스틱 최소 동작 횟수
def find_min(a):
    x = (a-1)
    y = abs(27-a)
    return min(x,y)

def solution(name):
    answer = 0
    name = list(name)
    name2 = []
    base = [1]*len(name)
    for el in name:
        name2.append(ord(el)-64)

    for el in range(0,len(base)):
        answer += find_min(name2[el])

    x = find_empty(name2)

    # 알파벳 A가 포함될 경우 왼쪽 서치 먼저, 오른쪽 서치 먼저, A문자열 가로지르기 중 최소 거리 구하기
    if 'A' in name:
        a = len(name2)-1-x[1]+2*(x[0]-1)
        b = len(name2)-1
        c = 2*(len(name2)-1-x[1])+x[0]-1
        tmp = min(a,b)
        tmp = min(tmp,c)
        answer += tmp

    else:
        answer += len(name2)-1

    return answer

name = 'JAN'
print(solution(name))