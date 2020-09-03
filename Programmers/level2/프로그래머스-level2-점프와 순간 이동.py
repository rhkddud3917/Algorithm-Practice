# -*- coding: utf-8 -*-
# 한 번에 K 칸을 앞으로 점프하거나, (현재까지 온 거리) x 2 에 해당하는 위치로 순간이동
# 점프하면 점프한 만큼 건전지 소모 따라서 순간이동 많이 하는게 좋음
# 이동하려는 거리에 대해 건전지 사용량 최솟값 반환

def solution(n):
    ans = 0

    while n != 0:
        b = n%2
        n = n//2
        if b == 1:
            ans += 1

    return ans

n = 5000
print(solution(n))