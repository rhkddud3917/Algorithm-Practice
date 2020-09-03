# -*- coding: utf-8 -*-
# 가로길이가 w 세로길이가 h 인 직사각형이 주어진다.
# 가로 1 세로 1 인 격자로 구성되어 있다.
# 왼쪽위 오른쪽아래 잇는 대각선 그었을 때 선이 지나가지 않는 격자의 수를 출력하시오.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def func(a,b):
    if a < b:
        c = b
        b = a
        a = c
    t = float(b)/float(a)
    count = a +b -1
    return count

def solution(w,h):
    x = gcd(w,h)
    a = w//x
    b = h//x
    if a == 1 or b == 1:
        square = a*b
        answer = w*h - x*square
    else:
        count = func(a,b)
        count = count * x
        answer = w*h - count
    return answer

w = 3
h = 5
print(solution(w,h))