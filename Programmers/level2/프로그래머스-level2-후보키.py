# -*- coding: utf-8 -*-
# 관계형 데이터베이스에서 후보키 쵀대 걔수
# 유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
# 최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다.
# 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.
# 다음 두 조건을 만족해야 함

from itertools import combinations
import copy

def solution(relation):

    col_len = len(relation[0])

    tmp = []
    candidate = []

    # 컬럼의 인덱스 리스트 생성
    for i in range(0,col_len):
        tmp.append(i)

    # 컴비네이션을 통해 컬럼의 모든 길이에 대한 조합의 결과가 후보키가 될 수 있는지 확인(유일성만 확인)
    for x in range(1,col_len+1):
        if len(tmp) < x: break
        com_tmp = list(combinations(tmp,x))

        for el in com_tmp:
            t = []
            for el3 in relation:
                v = []
                for el2 in el:
                    v.append((el2, el3[el2]))
                if v in t:
                    continue
                t.append(copy.deepcopy(v))
            if len(t) == len(relation):
                candidate.append(copy.deepcopy(el))

    # 희소성 확인
    j = 0
    while True:
        delList = []
        if j >= len(candidate): break
        for i in range(j+1,len(candidate)):
            for el in candidate[j]:
                no_del = 0
                if el not in candidate[i]:
                    no_del = 1
                    break
            if no_del == 0:delList.append(i)
        delList.reverse()
        for k in range(len(candidate)-1,j,-1):
            if k in delList:
                del candidate[k]
        j += 1

    answer = len(candidate)
    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],\
            ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))