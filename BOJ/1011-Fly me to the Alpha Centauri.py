# 이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다.
# 마지막은 무조건 1광년을 이동해야 한다.
# x 지점부터 y 지점까지 이동하는데 걸리는 최소 작동횟수를 출력

test = int(input())

for t in range(test):
    s,e = map(int,input().split(' '))
    dist = e - s
    n = 1
    while True:
        temp = (n*(n+1)+n*(n-1))//2
        if temp >= dist:
            break
        n += 1
    if temp == dist:
        print(n+n-1)
    else:
        n -= 1
        temp = (n*(n+1)+n*(n-1))//2
        if (dist-temp) <= n:
            print(n+n)
        else:
            print(n+n+1)

