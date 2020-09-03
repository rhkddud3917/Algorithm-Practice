# -*- coding: utf-8 -*-
# L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함
# 초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때,
# 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하라 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.

# 처음에는 리스트를 이용해서도 풀어보고 문자열을 이용해서도 풀어봤는데 시간초과가 떠서
# 입력과 pop에서 시간 복잡도가 O(1)인 deque를 두개를 사용해서 풀었다.
# deque는 커서를 기준으로 각각 왼쪽 문자들과 오른쪽 문자들을 저장하게 된다.
import sys
from collections import deque

s = (sys.stdin.readline().rstrip())
num = int(sys.stdin.readline().rstrip())

deq1 = deque(list(s))
deq2 = deque([])

for _ in range(num):
    temp = sys.stdin.readline().rstrip().split(' ')
    if temp[0] == 'L':
        if len(deq1) != 0:
            deq2.appendleft(deq1.pop())
    elif temp[0] == 'D':
        if len(deq2) != 0:
            deq1.append(deq2.popleft())
    elif temp[0] == 'B':
        if len(deq1) != 0:
            deq1.pop()
    else:
        deq1.append(temp[1])

sys.stdout.write(''.join(deq1)+''.join(deq2))

