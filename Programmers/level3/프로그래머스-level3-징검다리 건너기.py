# -*- coding: utf-8 -*-
# 징검다리는 일렬로 놓여 있고 각 징검다리의 디딤돌에는 모두 숫자가 적혀 있으며 디딤돌의 숫자는 한 번 밟을 때마다 1씩 줄어듭니다.
# 디딤돌의 숫자가 0이 되면 더 이상 밟을 수 없으며 이때는 그 다음 디딤돌로 한번에 여러 칸을 건너 뛸 수 있습니다.
# 단, 다음으로 밟을 수 있는 디딤돌이 여러 개인 경우 무조건 가장 가까운 디딤돌로만 건너뛸 수 있습니다.
# 디딤돌에 적힌 숫자가 순서대로 담긴 배열 stones와 한 번에 건너뛸 수 있는 디딤돌의 최대 칸수 k가 매개변수로 주어질 때,
# 최대 몇 명까지 징검다리를 건널 수 있는지 return

def solution(stones, k):

    l = 0
    r = max(stones)

    # 이분탐색을 이용해서 찾는다.
    # 탐색한 인원이 징검다리를 건널 수 있는지를 판단하여
    # 최대의 인원을 찾는다.
    while l <= r:

        mid = (l+r)//2
        count = 0
        leng = 0
        for el in stones:
            if el-mid <= 0:
                count += 1
                leng = max(leng,count)
            else:
                count = 0

        if leng < k:
            l = mid + 1

        elif leng >= k:
            r = mid - 1

    return l

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones,k))