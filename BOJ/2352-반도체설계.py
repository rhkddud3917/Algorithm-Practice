# n개의 포트가 다른 n개의 포트와 어떻게 연결되어야 하는지가 주어졌을 때,
# 연결선이 서로 꼬이지(겹치지, 교차하지) 않도록 하면서 최대 몇 개까지 연결할 수 있는지를 알아내는 프로그램을 작성
# 첫째 줄에 정수 n(1 ≤ n ≤ 40,000)이 주어진다.
# 다음 줄에는 차례로 1번 포트와 연결되어야 하는 포트 번호, 2번 포트와 연결되어야 하는 포트 번호, …, n번 포트와 연결되어야 하는 포트 번호가 주어진다.
# 이 수들은 1 이상 n 이하이며 서로 같은 수는 없다고 가정

n = int(input())

port = list(map(int,input().split()))

check = [0] * n
check[0] = 1
state = [0]
state.append(port[0])

for i in range(1,n):
    if port[i] > state[-1]:
        check[i] = len(state)
        state.append(port[i])
    else:
        l = 0
        r = len(state)-1
        find = 0
        while l <= r:
            mid = (l+r)//2
            if state[mid] <= port[i]:
                l = mid + 1
                if find < mid:
                    find = mid
            else:
                r = mid - 1
        state[find+1] = port[i]
        check[i] = find+1

print(len(state)-1)
