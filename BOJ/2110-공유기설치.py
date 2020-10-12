# 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성

n,c = map(int,input().split())
answer = 0

home = []
for i in range(n):
    home.append(int(input()))

home.sort()

l = 0
r = (home[-1]-home[0])//(c-1)
while l <= r:

    mid = (l+r)//2
    target = 100000000
    start = 0
    count = 1
    for i in range(len(home)):
        if home[i] - home[start] >= mid:
            if count == c-1:
                if target > home[-1] - home[start]:
                    target = home[-1] - home[start]
                start = n-1
                count += 1
                if count == c: break
            if target > home[i]-home[start]:
                target = home[i]-home[start]
            start = i
            count += 1

    if count < c:
        r = mid - 1

    elif count >= c:
        l = mid + 1
        answer = mid

print(answer)

