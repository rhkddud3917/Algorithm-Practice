# -*- coding: utf-8 -*-
# 앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
# 문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return

def solution(s):
    answer = 1

    i = 0
    while i<len(s):

        if i + 1< len(s):
            if s[i] == s[i+1]:
                count = 0
                while count <= i and count + 1 + i < len(s):
                    if s[i-count] != s[i+1+count]: break
                    count += 1
                if answer < count*2: answer = count *2
        if i+ 2< len(s):
            if s[i] == s[i+2]:
                count = 0
                while count <= i and count + 2 + i < len(s):
                    if s[i - count] != s[i + 2 + count]: break
                    count += 1
                if answer < count * 2 + 1: answer = count * 2 + 1

        i += 1

    return answer

s = 'abcde'
print(solution(s))