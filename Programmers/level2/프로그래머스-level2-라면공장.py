# -*- coding: utf-8 -*-
# 현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에 공급 가능한 밀가루 수량(supplies)
# k 일 전까지 공급을 받는 횟수의 최소 값을 반환
# 하루에 밀가루 1톤씩 사, k-1에 사용할 수량 까지만 확보하면 된다.
# 예를들어 현재 4가 남아있다면 오늘, 1일후, 2일, 3일후 까지만 사용할 수 있다. 4 일째에 공급 받아야 한다.

import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    index = 0
    heap = []
    while True:
        #heap = []
        # 재고가 떨어지면 가장 큰 공급량을 공급 받는다.
        for i in range(index, len(dates)):
            # 재고가 떨어지는지 확인
            if dates[i] <= stock:
                heapq.heappush(heap,(-supplies[i],dates[i],i))
                index = i+1
            # 재고가 떨어지면
            else:
                break
        answer += 1
        # 가장 큰 공급량을 받는다.
        x = heapq.heappop(heap)
        stock = stock -x[0]

        if stock >= k:
            break

    return answer


stock = 4
dates = [4,10,15]
supplies = [20,5,10]
k = 30
print(solution(stock,dates,supplies,k))