# -*- coding: utf-8 -*-
# 종이를 오른 쪽에서 왼쪽으로 절반씩 n 번 접고 난 후 펼쳤을 때
# 생기는 종이의 접힌 자국이 아래로 파져있으며 0, 위로 파져있으면 1
# 모든 접힌 모양에 대한 배열을 출력

# 접힐 때 기존의 접힌 자국이 순서가 뒤집히고 접히는 방향이 반대가 되므로 그것을 함수로 구현
def flip(l):
    l.reverse()
    for i in range(0,len(l)):
        if l[i] == 0 : l[i] = 1
        elif l[i] == 1: l[i] = 0
    return l

def solution(n):

    answer = [0]
    index = 1
    # 접을 때 가운데는 0 이생기고 왼쪽 오른쪽으로 flip 된 모양이 나타남 
    while True:
        if index >= n: break
        answer = answer + [0] + flip(answer)
        index += 1

    return answer

n = 3
print(solution(n))