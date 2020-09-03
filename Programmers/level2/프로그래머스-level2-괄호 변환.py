# -*- coding: utf-8 -*-
# (, ) 수가 같으면 균형잡힌 문자열
# 짝도 맞으면 올바른 문자열
# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.
# 균형잡힌 괄호 문자열 p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 올바른 괄호 문자열로 변환한 결과를 return

from collections import deque

def right_check(l):
    test = 0
    l = list(l)
    while True:
        x = l.pop(0)
        if x == '(': test += 1
        else: test -= 1
        if test < 0: return False
        if len(l) == 0: break
    return True

def semi(p,answer):
    if p == '': return ''
    l_num = 0
    r_num = 0
    for i in range(0,len(p)):
        if p[i] == '(': l_num += 1
        elif p[i] == ')': r_num += 1
        if l_num == r_num:
            index = i
            break
    u = p[0:index+1]
    v = p[index+1:]

    if right_check(u):
        answer += u + semi(v,answer)
    else:
        u = u[1:len(u)-1]
        tmp = ''
        for i in range(0,len(u)):
            if u[i] == '(' :tmp+= ')'
            else: tmp += '('
        answer += '(' + semi(v,answer) + ')' + tmp
    return answer

def solution(p):
    answer = ''
    answer = semi(p,answer)
    return answer

p = "()((()))))))((((()"
print(solution(p))
