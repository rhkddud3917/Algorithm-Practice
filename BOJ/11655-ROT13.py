# -*- coding: utf-8 -*-
# ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.
# ROT13은 알파벳 대문자와 소문자에만 적용할 수 있다. 알파벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다.

s = input()
res = ''

for el in s:
    if (ord('A') <= ord(el) and ord(el) <= ord('Z')):
        if ord(el) + 13 > ord('Z'):
            target = ord('A') + ord(el) + 13 - ord('Z') -1
        else:
            target = ord(el) + 13
        res += chr(target)
    elif (ord('a') <= ord(el) and ord(el) <= ord('z')):
        if ord(el) + 13 > ord('z'):
            target = ord('a') + ord(el) + 13 - ord('z') -1
        else:
            target = ord(el) + 13
        res += chr(target)
    else:
        res += el

print(res)