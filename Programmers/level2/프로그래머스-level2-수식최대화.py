# -*- coding: utf-8 -*-
# 수식에서 연산자의 우선순위를 정하여 가장 최대의 결과를 낸다.
# 결과가 음수면 절대값을 씌운다.
# 우선순위가 같은 것이 있으면 안된다.

from itertools import permutations
import re
import copy

# 보내진 우선순위 대로 수식을 계산
def calculate(numbers, ops, order):
    for el in order:
        while True:
            flag = 0
            for i in range(0,len(ops)):
                if ops[i] == el and el == '+':
                    numbers[i] = int(numbers[i]) + int(numbers[i+1])
                    del numbers[i+1]
                    del ops[i]
                    flag = 1
                    break
                elif ops[i] == el and el == '-':
                    numbers[i] = int(numbers[i]) - int(numbers[i + 1])
                    del numbers[i+1]
                    del ops[i]
                    flag = 1
                    break
                elif ops[i] == el and el == '*':
                    numbers[i] = int(numbers[i]) * int(numbers[i + 1])
                    del numbers[i+1]
                    del ops[i]
                    flag = 1
                    break
            if flag == 0: break

    return numbers[0]

def solution(expression):

    op = ['+', '-', '*']
    opList = list(permutations(op,3))

    # 숫자들 리스트와 연산자들 리스트 생성
    numbers = re.split('\D+', expression)
    ops = re.split('\d+', expression)
    ops = ops[1:-1]

    answerList = []

    # 우선순위들 경우의 수 만큼 계산을 하고 가장 큰 값을 뽑음
    for el in opList:
        num = copy.deepcopy(numbers)
        o = copy.deepcopy(ops)
        answerList.append(calculate(num,o, el))

    for i in range(0,len(answerList)):
        if answerList[i] < 0 : answerList[i] = abs(answerList[i])

    answer = max(answerList)

    return answer

expression = "100-200*300-500+20"
print(solution(expression))