# -*- coding: utf-8 -*-
# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

import copy

def solution(arr1, arr2):
    answer = []

    # 행렬의 곱 답 에 해당하는 list 만들기
    for i in range(0,len(arr1)):
        temp = []
        for j in range(0,len(arr2[0])):
            temp.append(0)
        answer.append(copy.deepcopy(temp))

    # 답의 원소에 행렬의 곱 규칙대로 숫자를 하나씩 채워넣는다.
    for i in range(0,len(answer)):
        for j in range(0,len(answer[0])):
            for k in range(0,len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]


    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1,arr2))