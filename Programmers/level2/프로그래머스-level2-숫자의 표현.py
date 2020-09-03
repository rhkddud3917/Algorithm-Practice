# -*- coding: utf-8 -*-
# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return

def solution(n):
    # 자기 자신 숫자도 답에 포함 되므로 1로 시작을 한다.
    answer = 1

    # 1부터 시작해서 연속되는 숫자로 표현할 수 있는지 확인을 한다.
    # 시작하는 수가 원래의 수의 반을 넘기면 표현이 불가능하므로 효율성을 위해 break 로 반복문을 탈출한다.
    start = 1
    while True:
        if start > n//2: break
        i = 0
        res = 0
        while True:
            res += (start + i)
            if res == n:
                answer += 1
            elif res > n: break
            i += 1
        start += 1

    return answer

n = 15
print(solution(n))