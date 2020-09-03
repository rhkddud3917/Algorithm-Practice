T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    line = []
    for _ in range(num):
        temp = list(map(int,input().split(' ')))
        line.append(temp)
    line.sort()
    res = 0
    for i in range(num):
        j = 1
        while i+j < num:
            if line[i][1] > line[i+j][1]:
                res += 1
            j += 1
    print('#'+str(test_case),res)
