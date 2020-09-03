# -*- coding: utf-8 -*-
# 아이디 목록이 주어지고 불량 사용자의 목록이 주어진다.
# 불량사용자의 아이디는 일부 문자가 * 로 표시가 되어 있다. 이 * 에는 어느 문자든 올 수 있다.
# 불량사용자 아이디경우 하나당 하나의 아이디만 목록에 포함 가능
# 제재되는 아이디 목록의 총 경우의 수 리턴

from itertools import product
from collections import deque
import re

def solution(user_id, banned_id):

    # 정규식을 이용해서 banned_id들 각각에 해당하는 아이디들을 모은다.
    my_list = deque([])
    for b in banned_id:
        b = b.replace('*','.')
        tmp = deque([])
        for u in user_id:
            if len(b) == len(u):
                if re.compile(b).match(u):
                    tmp.append(u)
        my_list.append(tmp)

    # product 를 사용해서 모든 경우의수를 만든다.
    x = list(product(*my_list))

    answer = set()

    # 경우의 수 들 중에서 겹치지 않는 것을 선정한다.
    for el in x:
        el = frozenset(el)
        if len(el) == len(my_list):
            answer.add(el)

    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
print(solution(user_id,banned_id))