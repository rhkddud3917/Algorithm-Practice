# -*- coding: utf-8 -*-
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성

s = input().split(' ')
a, b = int(s[0]), int(s[1])

def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

if a < b:
    tmp = b
    b = a
    a = tmp

print(gcd(a,b))
print(a//gcd(a,b)*b)