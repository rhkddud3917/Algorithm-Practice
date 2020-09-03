# -*- coding: utf-8 -*-
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성

import sys
from collections import deque

n,k = (sys.stdin.readline().rstrip().split(' '))
n,k = int(n),int(k)

people = deque(list(k for k in range(1,n+1)))

# deque을 이용해서 앞에서 빼고 뒤에 다시 넣는 것을 반복하다가 k 번째인 수는 정답에 추가를 하였다.
res = deque([])
while len(people) > 0:
    for _ in range(k-1):
        people.append(people.popleft())
    res.append(people.popleft())

ans = '<'
for el in res:
    ans += str(el)+', '
ans = ans[:-2] + '>'
print(ans)