# -*- coding: utf-8 -*-
# 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return\
# clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
#스파이는 하루에 최소 한 개의 의상은 입습니다.


def solution(clothes):
    answer = 0

    hash_kind = {}
    for el in clothes:
        try:
            hash_kind[el[1]].append(el[0])
        except:
            hash_kind[el[1]] = [el[0]]

    x = 1
    for el in hash_kind.keys():
        x *= len(hash_kind[el])+1
    x -= 1
    answer = x
    return answer

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))