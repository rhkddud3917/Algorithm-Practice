# -*- coding: utf-8 -*-
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return

from functools import cmp_to_key

# < = -1 , > = 1 , == = 0
def comp(a,b):
    i = 0
    # 길이가 다른 문자열에서 긴 문자열의 나머지 부분과 짧은 문자열의 앞부분을 다시 비교하여 크기 비교를 했다.
    while i<=4:
        p = a[i%len(a)]
        q = b[i%len(b)]

        if p < q : return -1
        elif p > q : return 1

        i += 1
    return 0

def solution(numbers):
    for i in range(0,len(numbers)):
        numbers[i] = str(numbers[i])
    numbers = sorted(numbers, key=cmp_to_key(comp))
    numbers.reverse()
    result = []
    for el in numbers:
        result.append(str(el))
    answer = ''.join(result)
    for i in range(0,len(answer)-1):
        if answer[0] == '0':
            answer = answer[1:]
    return answer

numbers = [0,0,0,0,0]
print(solution(numbers))