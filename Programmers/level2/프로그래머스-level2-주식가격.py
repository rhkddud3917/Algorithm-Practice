# -*- coding: utf-8 -*-
# 초단위로 주식이 주어질 때 각 자리 마다 가격이 떨어지지 않은 초 만큼을 리턴하시오
# prices	        return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

def solution(prices):
    answer = []
    for el in prices:
        answer.append(0)
    for i in range(0,len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                answer[i]+= 1
                break
            else:
                answer[i] += 1
    return answer

prices = [1,2,3,2,3]
print(solution(prices))