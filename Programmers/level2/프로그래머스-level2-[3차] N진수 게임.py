# -*- coding: utf-8 -*-
# 숫자를 1씩 늘리는 대신 숫자를 하나씩 만 말하는 데 진법을 추가하기로 함
# 자신이 말해야 하는 숫자를 출력하는 프로그램 작성
# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.

# 숫자를 n 진수로 바꿔주는 함수
def make_n(n,num):
    res = ''
    while True:
        if num >= n:
            if num % n == 10: res = 'A' + res
            elif num % n == 11: res = 'B' + res
            elif num % n == 12: res = 'C' + res
            elif num % n == 13: res = 'D' + res
            elif num % n == 14: res = 'E' + res
            elif num % n == 15: res = 'F' + res
            else: res = str(num % n) + res
            num = num // n
        else:
            if num == 10: res = 'A' + res
            elif num == 11: res = 'B' + res
            elif num == 12: res = 'C' + res
            elif num == 13: res = 'D' + res
            elif num == 14: res = 'E' + res
            elif num == 15: res = 'F' + res
            else: res = str(num) + res
            break
    return res

def solution(n, t, m, p):
    answer = ''
    total = ''
    # 전체 숫자열 생성
    for i in range(0,m*t):
        total += make_n(n,i)

    # 전체 숫자열 중에서 주어진 조건의 숫자만 추출
    count = 0
    for i in range(0,len(total)):
        if i % m == p-1:
            answer += total[i]
            count += 1
        if count == t: break
    return answer

n = 2
t = 4
m = 2
p = 1
print(solution(n,t,m,p))