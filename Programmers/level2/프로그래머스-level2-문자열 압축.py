# -*- coding: utf-8 -*-
# 1개 이상 단위로 문자열을 압축한 것 중에 가장 짧은 것을 반환하라
# ababcdcdababcdcd -> 2abcdede
# 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.

def solution(s):
    answer = 10000
    l = len(s) / 2
    if len(s) == 1: return 1

    # 잘라지는 모든 길이의 단위 적용
    for i in range(1,l+1):
        str1 = []
        # 단위길이에 맞게 스트링 자르기
        for j in range(0, len(s), i):
            if j+i > len(s)-1:
                str1.append(s[j:len(s)])
            else:
                str1.append(s[j:j+i])

        str2 = [0] * len(str1)
        # 새로운 리스트에 반복되는 문자단위 표시 앞뒤가 반복되면 1
        for el in range(0,len(str1)-1):
            if str1[el] == str1[el+1]:
                str2[el] = 1

        # 반복되는 횟수 적용하기 최초를 제외한 반복되는 문자단위는 -1로 처리
        for el in range(0,len(str2)):
            if str2[el] == 0: continue
            elif str2[el] == 1:
                tmp = el+1
                while str2[tmp] != 0:
                    tmp += 1
                str2[el] = tmp-el+1
                for el2 in range(el+1,tmp+1):
                    str2[el2] = -1

        # 반복되는 문자단위 제거
        delList = []
        for el in range(0,len(str2)):
            if str2[el] == 0 : continue
            elif str2[el] == -1 : delList.append(el)
            else:
                str1[el] = str(str2[el]) + str1[el]

        delList.reverse()
        for el in delList:
            del str1[el]

        res = len(''.join(str1))
        if answer > res: answer = res

    return answer

s = "a"
print(solution(s))