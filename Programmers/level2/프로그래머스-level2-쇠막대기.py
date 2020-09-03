# -*- coding: utf-8 -*-
# () 는 레이저이다
# ( 는 막대기의 시작 부분 ) 는 막대기의 끝 부분이다.
# 큰 막대기는 작은 막대기 위에 놓을 수 없다.
# 잘려진 조각의 수를 출력하라

def solution(arrangement):
    answer = 0
    arr = list(arrangement)
    count = 0

    while True:
        x = arr.pop(0)
        if x == ')':
            answer += 1
            count -= 1
        if len(arr) == 0:
            break
        y = arr[0]
        if x == '(' and y == '(':
            count += 1
        if x == '(' and y == ')':
            answer += count
            del arr[0]

    return answer

arrangement = "()(((()())(())()))(())"
print(solution(arrangement))