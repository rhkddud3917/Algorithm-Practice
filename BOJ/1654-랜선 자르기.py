# -*- coding: utf-8 -*-
# K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다.
# 박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다.
# 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm 은 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성
# 입력: K N K <= N 이다.

s = input().split(' ')
k = int(s[0])
n = int(s[1])

lineList = []
for i in range(0,k):
    lineList.append(int(input()))
lineList.sort()

answer = 0

l = 1
r = lineList[-1]
while l <= r:
    tmp = (l+r)//2
    res = 0
    for el in lineList:
        res += el//tmp
    if res >= n:
        l = tmp+1
    elif res < n:
        r = tmp-1

print(r)
