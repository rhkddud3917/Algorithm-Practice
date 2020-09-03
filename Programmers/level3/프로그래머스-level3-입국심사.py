# -*- coding: utf-8 -*-
# 처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다.
# 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다.
# 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.
# 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.
# 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때 최소 시간 반환

def solution(n, times):

    l = 0
    r = n * max(times)
    # 이분 탐색을 하여서 해당 시간에 대해 처리하는 사람의 수를 count 에 저장한다.
    # count 와 n 의 값을 비교하여 모든 사람을 심사하는 최소 시간을 반환한다.
    while r >= l:
        mid = (l+r)//2
        count = 0
        for el in times:
            count += mid // el
        if count < n:
            l = mid + 1
        elif count >= n:
            r = mid - 1

    return l

n = 6
times = [7, 10]
print(solution(n,times))