# -*- coding: utf-8 -*-
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

def solution(number,k):
    start = 0
    res = []
    length = len(number)
    last_index = length
    while k!=0:
        max = -1
        # 제일 뒤의 범위 까지 갔을 때 제거해야 할 숫자가 모두 제거 되지 않았다면 뒤의 수들을 해당 수만큼 제거한다.
        if start + k + 1 > length:
            last_index = length - k
            break
        # 인덱스 0 부터 시작하여 제거해야할 수의 개수 + 1 까지의 범위에서 최대 값을 찾는다. 해당 최대값의 인덱스 저장
        # 인덱스를 저장한 것 다음 부터 남은 개수 + 1 까지 를 범위로 최대 값을 또 찾는다.
        # start 를 이용해서 처음 인덱스를 계속 업데이트 해가면서 while 문을 통해
        # 제거해야 할 수의 개수를 모두 제거할 때까지 반복한다.
        for i in range(start,start+k+1):
            if max < int(number[i]):
                max = int(number[i])
                idx = i
                if max == 9: break

        res.append(number[idx])
        k = k - (idx-start)
        start = idx+1

    return ''.join(res)+number[idx+1:last_index]

number = "000010000"
k = 2
print(solution(number,k))