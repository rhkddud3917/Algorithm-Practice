# -*- coding: utf-8 -*-
# 정해진 길이 보다 높은 나무만 자른다.
# 잘라진 나무의 총합이 목표치를 충족해야 할 때
# 정해진 길이 보다 높은 나무들을 자르기 위한 정히진 길이의 최대값 구하기
# 나무의 수 목표치 \n 나무들의 길이 입력

s = input().split(' ')
n,m = int(s[0]), int(s[1])

tree = input().split(' ')
for i in range(0,len(tree)):
    tree[i]= int(tree[i])

l ,r = 0, max(tree)

# 이분 탐색으로 길이를 탐색했다.
# 목표치에 딱 맞지 않게 나올 수 있으므로
# 목표를 충족하는 최대 값을 반환하였다.
while l <= r:
    mid = (l+r)//2
    res = 0
    for el in tree:
        if el > mid:
            res += el-mid
    if res >= m:
        l = mid +1
    elif res < m:
        r = mid -1

print(r)