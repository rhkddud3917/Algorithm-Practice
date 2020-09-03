# -*- coding: utf-8 -*-
# 모든 수를 1 2 4 만을 사용해서 나타낸다.
# 십진 수를 124 나라의 수로 변환하라.
# 1 2 4 11 12 14 21 22 24 41 42 44 이런식으로 된다. 점점 커지는 방향으로 순서대로 1,2,3 ...

def solution(n):
    n = int(n)
    k = n-1
    answer = []
    flag = 0
    while True:
        if k % 3 == 0: x = 1
        if k % 3 == 1: x = 2
        if k % 3 == 2: x = 4
        answer.insert(0,str(x))
        if flag == 1: break
        k = k//3 - 1
        if k < 3: flag = 1

    answer = ''.join(answer)
    return answer

print(solution('12'))