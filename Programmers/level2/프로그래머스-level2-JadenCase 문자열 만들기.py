# -*- coding: utf-8 -*-
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
# 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다.

def solution(s):

    s = s.split(' ')
    for i in range(0,len(s)):
        new_str = ''
        for j in range(0,len(s[i])):
            # 첫 글자가 숫자이면 그대로 아니면 대문자로 바꾼다.
            if j == 0:
                if s[i][j] not in '1234567890':
                    new_str += s[i][j].upper()
                else:
                    new_str += s[i][j]
            # 나머지 글자가 숫자면 그대로, 아니면 소문자로 바꾼다.
            else:
                if s[i][j] not in '1234567890':
                    new_str += s[i][j].lower()
                else:
                    new_str += s[i][j]
        s[i] = new_str

    answer = ' '.join(s)
    return answer

s =  '3people unFollowed me'
print(solution(s))