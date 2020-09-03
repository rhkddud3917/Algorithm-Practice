# -*- coding: utf-8 -*-
# 문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.
# baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지

s = input()

res = []
for i in range(len(s)):
    res.append(s[i:])

res.sort()

for el in res:
    print(el)