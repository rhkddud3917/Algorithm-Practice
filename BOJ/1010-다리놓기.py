# 강의 서쪽에 N개의 점, 동쪽에 M개의 점 있다.
# N <= M 이다.
# 최대한 많은 다리를 놓으려 할 때 총 경우의 수는?

test = int(input())

for t in range(test):
    n, m = map(int,input().split(' '))
    if n == m: print(1)
    else:
        ans = 1
        div = 1
        for i in range(m,m-n,-1):
            ans *= i
        for i in range(1,n+1):
            div *= i
        print(ans//div)