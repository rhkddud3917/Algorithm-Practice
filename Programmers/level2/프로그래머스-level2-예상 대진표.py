# -*- coding: utf-8 -*-
# 1 - n 번까지 번호 부여 받음
# 옆번호와 대결 진행 이긴자들 순서대로 1 - n/2 번 번호 부여 받음
# 두 선수가 몇 번째 라운드에서 만날지 반환 대신 계속 이긴다고 가정

def solution(n,a,b):
    answer = 0
    # 번호를 0 부터 시작하게 맞춤
    a -= 1
    b -= 1

    # 여기서 카운트가 둘이 시합하고 난 후 까지 세기 때문에 1을 빼줘야함
    # 그래서 처음부터 0회전 부터시작하는 것으로 적용
    while a != b:
        a = a//2
        b = b//2
        answer += 1

    return answer

n = 8
a = 4
b = 7
print(solution(n,a,b))