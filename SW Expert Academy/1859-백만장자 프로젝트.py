T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    price = list(map(int,input().split(' ')))
    res = 0
    sell = 0
    for i in range(num-1,-1,-1):
        if price[i] > sell:
            sell = price[i]
        else:
            res += sell-price[i]
    print("#"+str(test_case),res)