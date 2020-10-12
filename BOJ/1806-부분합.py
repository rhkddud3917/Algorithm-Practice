# -*- coding: utf-8 -*-
# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
# 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
# 첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.

n, val = map(int,input().split())

target = list(map(int,input().split()))

l = 1
r = n
answer = 100000000

if sum(target) < val : print(0)

else:

    res = target[0]
    s = 0
    e = 0
    while True:
        if res >= val:
            if answer > e-s+1:
                answer = e-s+1
            res -= target[s]
            s += 1


        elif res < val:
            if e == n-1: break
            e += 1
            res += target[e]

    print(answer)


