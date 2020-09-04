# 둘은 서로의 차례에 인접한 두 자리를 선택하고, 이 두 자리를 선택된 두 숫자의 합으로 교체하여 상대에게 차례를 넘긴다.
# 예를 들어, “1234”의 십의 자리와 백의 자리를 선택하면 다음 차례에는 수가 “154”가 된다.
# “5678”의 십의 자리와 백의 자리를 선택하면 다음 차례에는 수가 “5138”이 된다.
# 이렇게 차례를 반복 하다가 자기 차례에 넘어온 수가 한 자리가 되면 그 사람이 패배하게 된다.
# 누가 이길지 판단하는 프로그램 작성
# A,B 중 A가 먼저 시작
T = int(input())
for test_case in range(1, T + 1):
    num = list(map(int,input()))
    i = 0
    while len(num) != 1:
        a = num.pop()
        b = num.pop()
        res = a+b
        if res >= 10:
            num.append(res//10)
            num.append(res%10)
        else:
            num.append(res)
        i += 1
    ans = 'A'
    if i % 2 == 0: ans = 'B'
    print('#'+str(test_case)+' '+ans)