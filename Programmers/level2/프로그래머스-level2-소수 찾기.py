# -*- coding: utf-8 -*-
# 주어진 숫자들을 이용해서 만들 수 있는 소수의 개수를 반환

from itertools import permutations

# 소수 확인
def check(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def solution(numbers):
    answerList = []
    numbers = list(numbers)
    # 문자열이 7까지이므로 1부터7까지 경우 돌림
    for i in range(1,8):
        checkList = list(permutations(numbers,i))
        realList = []
        # 퍼뮤테이션 돌린 것 원하는 모양으로 바꿈
        for el in checkList:
            str1 = ''
            for e in el:
                str1 = str1+e
            realList.append(str1)
        # 1이거나 0 이거나 0으로 시작하는 것 제외 나머지 소수인지 판별
        for el in realList:
            if el == '0': continue
            elif el == '1': continue
            elif el[0:1] == '0' : continue
            elif check(int(el)):
                answerList.append(el)

    answerList = list(set(answerList))
    answer = len(answerList)
    print(answerList)
    return answer

numbers = '11'
print(solution(numbers))