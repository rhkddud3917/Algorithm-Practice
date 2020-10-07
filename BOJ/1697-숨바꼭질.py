# x+1, x-1, 2x 위치로 1초마다 갈 수 있다.
# 도착점까지 가는데 최단시간 출력

from collections import deque

start, end = list(map(int,input().split()))
check = [0] * end*2

queue = deque([])
queue.append(start)
count = 0
if start == end:
    print(0)

elif start > end:
    print(start-end)

else:
    while len(queue) != 0:
        #print(queue)
        success = 0
        l = len(queue)
        for i in range(l):
            x = queue.popleft()
            if 0 <= x-1 <= 2*max(start,end) and check[x-1] == 0:
                queue.append(x-1)
                check[x-1] = 1
                if x-1 == end:
                    success = 1
                    break
            if 0 <= x + 1 <= 2 * max(start, end) and check[x+1] == 0:
                queue.append(x+1)
                check[x+1] = 1
                if x+1 == end:
                    success = 1
                    break
            if 0 <= 2*x <= 2 * max(start, end) and check[x*2] == 0:
                queue.append(2*x)
                check[2*x] = 1
                if x*2 == end:
                    success = 1
                    break

        count += 1
        if success == 1: break

    print(count)