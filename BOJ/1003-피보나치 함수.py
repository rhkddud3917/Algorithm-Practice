# 피보나치 수열에서 특정 숫자를 입력할때
# 정석적인 피보나치 수열 계산에서 특정 숫자번째의 피보나치 수열은
# 피보나치 수열의 0 번째와 1번째를 총 몇 번 방문하게 되는지 출력

test = int(input())

# 다이나믹 프로그래밍을 이용했다.
dict = {}
dict[0] = [1,0]
dict[1] = [0,1]
for t in range(test):

    n = int(input())
    if n == 0:
        print(dict[0][0],dict[0][1])
    elif n == 1:
        print(dict[1][0],dict[1][1])
    else:
        try:
            print(dict[n][0],dict[n][1])
        except:
            for i in range(2,n+1):
                dict[i] = [dict[i-1][0]+dict[i-2][0],dict[i-1][1]+dict[i-2][1]]
            print(dict[n][0],dict[n][1])
