# -*- coding: utf-8 -*-
# 2개의 짝이 있는 문자들을 제거하고 앞뒤로 붙인다.
# 모두 제거가 가능하면 1 아니면 0 반환

from collections import deque

def solution(s):

    x = deque()

    # 스택을 이용해서 값을 넣을 때마다 계속 스택을 갱신했다.
    # 짝이 맞으면 pop을 한다.
    for el in s:
        deque.append(x,el)
        if len(x) >= 2:
            while x[len(x)-1] == x[len(x)-2] and len(x) >= 2:
                deque.pop(x)
                deque.pop(x)
                if len(x) == 0: break

    if len(x) == 0: return 1
    else: return 0

s = "baabaa"
print(solution(s))
