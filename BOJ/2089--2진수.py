# -*- coding: utf-8 -*-
# 10진법의 수를 입력 받아서 -2진수를 출력하는 프로그램을 작성

import math

num = int(input())
answer = ''

if num == 0: print('0')
else:
    # 기존의 진법을 구하는 방법에서 나머지가 0,1 만 나오도록 변형시켰다.
    while num != 1:
        p = math.ceil(num/-2)
        q = num - (-2 * p)
        answer = str(q) + answer
        num = p

    print('1' + answer)