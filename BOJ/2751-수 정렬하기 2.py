# -*- coding: utf-8 -*-
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

num = int(input())

res = []
for _ in range(num):
    res.append(int(input()))

res.sort()

for el in res:
    print(el)