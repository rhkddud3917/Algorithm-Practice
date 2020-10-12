# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

s = int(input())

l = 1
r = s
answer = 0

while l <= r:

    mid = (l+r)//2

    add = mid*(mid+1)//2

    if add <= s:
        l = mid + 1
        answer = mid

    elif add > s:
        r = mid - 1

print(answer)