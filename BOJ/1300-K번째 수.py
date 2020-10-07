# 세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다.
# 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.
# 배열 A와 B의 인덱스는 1부터 시작한다.

n = int(input())
k = int(input())

l = 1
r = n**2
ans = 0

while True:
    mid = (l+r)//2
    low = 0
    same = 0

    for i in range(1,min(mid+1,n+1)):
        if mid % i != 0:
            low += min((mid // i),n)
        else:
            low += min((mid // i),n)
            if mid // i <= n:
                low -= 1
                same += 1

    if low + same < k:
        l = mid + 1

    elif k <= low:
        r = mid - 1

    elif low < k <= low + same:
        ans = mid
        break

print(ans)