# -*- coding: utf-8 -*-
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 반환

from itertools import combinations

# 소수인지 체크하는 함수
def check(n):
    m = sum(n)
    for i in range(2,m):
        if m/i == int(m/i): return False
    return True

def solution(nums):
    answer = 0
    # 숫자 세개를 뽑는 모든 조합
    nums = list(combinations(nums,3))
    for el in nums:
        x = check(el)
        # 소수면 답에 1더하기
        if x: answer += 1

    return answer

nums = [1,2,3,4]
print(solution(nums))