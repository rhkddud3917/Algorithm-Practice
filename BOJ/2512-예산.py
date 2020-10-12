# 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
# 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
# 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.

n = int(input())
need = list(map(int,input().split()))
money = int(input())

l = 0
r = money
answer = 0

if sum(need) <= money:
    print(max(need))
else:
    while l <= r:

        mid = (l+r)//2

        count = 0
        for el in need:
            if el <= mid:
                count += el
            else:
                count += mid

        if count <= money:
            l = mid + 1
            if answer < mid:
                answer = mid
        else:
            r = mid - 1

    print(answer)