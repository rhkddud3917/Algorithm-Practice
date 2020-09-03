# -*- coding: utf-8 -*-
# 괄호가 올바르면 true, 아니면 false 반환

from collections import deque

def solution(s):
    # 스택을 이용해서 구현을 하였다.
    # 짝이 맞으면 에러 없이 빈 스택을 내보낼 것이다.
    # pop 에서 에러가 발생하거나 빈 스택이 아니면 잘못된 괄호이다.
    dq = deque()
    for el in s:
        if el == '(':
            dq.append('(')
        else:
            try:
                dq.pop()
            except:
                return False

    if len(dq) == 0: return True
    else: return False
