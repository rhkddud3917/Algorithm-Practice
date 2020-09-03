# -*- coding: utf-8 -*-
# N 마리 폰켓몬 중에 N/2 마리 만큼 선택을 하는데
# 같은 종류의 폰켓몬은 같은 번호를 가지고 있다.
# 가장 많은 종류를 선택하 종류의 개수를 반환

def solution(nums):
    n = len(nums)
    n = n/2

    # 종류 수가 N/2 보다 많으면 N/2를 리턴
    # 아니면 종류 수를 리턴
    nums = list(set(nums))
    if len(nums) >= n: return n
    else: return len(nums)

nums = [3,1,2,3]
print(solution(nums))