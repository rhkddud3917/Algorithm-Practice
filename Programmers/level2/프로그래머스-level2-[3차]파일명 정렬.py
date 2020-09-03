# -*- coding: utf-8 -*-
# 파일명은 크게 HEAD, NUMBER, TAIL의 세 부분으로 구성된다.
# HEAD는 숫자가 아닌 문자로 이루어져 있으며, 최소한 한 글자 이상이다.
# NUMBER는 한 글자에서 최대 다섯 글자 사이의 연속된 숫자로 이루어져 있으며, 앞쪽에 0이 올 수 있다.
# 0부터 99999 사이의 숫자로, 00000이나 0101 등도 가능하다.
# TAIL은 그 나머지 부분으로, 여기에는 숫자가 다시 나타날 수도 있으며, 아무 글자도 없을 수 있다.
# 1. head 알파벳 순으로 정렬 대소문자 비교 안함
# 2. head 같으면 number 순서대로 정렬 numbers 에서 앞의 0들은 무시
# 3. number 까지 같으면 들어온 순서대로 즉 tail은 비교 안함

import re

def solution(files):
    answer = []
    order = []
    x = 0
    for el in files:
        index = 0
        tmp = []
        # head 부분 추출
        while True:
            if re.compile('\d').match(el[index]) != None:
                break
            index += 1
        tmp.append(el[0:index].lower())

        # number 부분 추출
        count = 0
        while True:
            if index+count >= len(el) or count > 4 or re.compile('\d').match(el[index+count]) == None:
                break
            count += 1
        tmp.append(int(el[index:index+count]))
        # 들어온 순서 추출
        tmp.append(x)
        order.append(tmp)
        x += 1

    # 조건의 순서대로 정렬
    order = sorted(order, key=lambda x: (x[0],x[1],x[2]))
    for el in order:
        answer.append(files[el[2]])
    return answer

files = ['F-511111 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']
print(solution(files))