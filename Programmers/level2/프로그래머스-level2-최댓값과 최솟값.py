# -*- coding: utf-8 -*-
# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다.
# str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 (최소값) (최대값)형태의 문자열을 반환

def solution(s):
    s = s.split(' ')
    for i in range(0,len(s)):
        s[i] = int(s[i])

    return str(min(s)) + ' ' + str(max(s))
s = "1 2 3 4"
print(solution(s))