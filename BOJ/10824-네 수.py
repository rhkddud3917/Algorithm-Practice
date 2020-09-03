# -*- coding: utf-8 -*-
# 네 자연수 A, B, C, D가 주어진다. 이때, A와 B를 붙인 수와 C와 D를 붙인 수의 합을 구하는 프로그램을 작성하시오.

s = input().split(' ')

num1 = int(s[0]+s[1])
num2 = int(s[2]+s[3])

print(num1+num2)