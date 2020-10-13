# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 30, 50} 이고, 길이는 4이다.

n = int(input())

num = list(map(int,input().split()))

check = [0]*n
check[0] = 1

lower_bound = []
lower_bound.append(0)
lower_bound.append(num[0])

for i in range(1,n):
    if lower_bound[-1] < num[i]:
        check[i] = len(lower_bound)
        lower_bound.append(num[i])
    else:
        l = 0
        r = len(lower_bound)-1
        find = 0
        while l <= r:
            mid = (l+r)//2
            if lower_bound[mid] < num[i]:
                l = mid + 1
                if find < mid:
                    find = mid
            else:
                r = mid - 1
        check[i] = find+1
        lower_bound[find+1] = num[i]

print(len(lower_bound)-1)

