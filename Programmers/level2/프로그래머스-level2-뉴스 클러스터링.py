# -*- coding: utf-8 -*-
# 두 집합 A, B 사이의 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의
# 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. ( 중복 허용 )
# 이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다.
# 다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. AB와 Ab, ab는 같은 원소로 취급한다.
# 자카드 유사도에 65536를 곱한 후 반환

import re

def solution(str1, str2):

    str1 = str1.upper()
    str2 = str2.upper()

    s1 = []
    s2 = []

    # 알파벳을 제외한 문자나 숫자들 리스트 생성
    selected1 = re.findall('\W', str1) + list('0123456789')
    selected2 = re.findall('\W', str2) + list('0123456789')

    selected1.append('_')
    selected2.append('_')

    # 알파벳이 아니면 추가하지 않음
    for i in range(len(str1) - 1):
        if str1[i] not in selected1 and str1[i + 1] not in selected1:
            a = str1[i] + str1[i + 1]
            s1.append(a.upper())
    for i in range(len(str2) - 1):
        if str2[i] not in selected2 and str2[i + 1] not in selected2:
            a = str2[i] + str2[i + 1]
            s2.append(a.upper())
    inner = []
    outer = []

    # 교집합 구하기
    for el in s1:
        tmp = len(s2)
        for i in range(tmp-1,-1,-1):
            if el == s2[i]:
                del s2[i]
                inner.append(el)
                break

    for el in inner:
        s1.remove(el)

    outer = s1 + s2 + inner

    # 예외처리
    if len(inner) == 0 and len(outer) == 0: return 65536
    if len(inner) == 0: return 0
    if len(outer) == 0: return 65536

    answer = int(65536 * (len(inner)/len(outer)))
    return answer

str1 = "FRrrANCE~!@#$%^&*()_ +"
str2 = "frrrrench"
print(solution(str2,str1))