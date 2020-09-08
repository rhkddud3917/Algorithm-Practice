# n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력

T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    money = list(map(int,input().split(' ')))
    sum = 0
    for el in money:
        sum += el
    avg = sum / num
    res = 0
    for el in money:
        if avg >= el:
            res += 1
    print('#'+str(test_case),res)