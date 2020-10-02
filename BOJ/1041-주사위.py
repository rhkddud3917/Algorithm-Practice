# n*n*n개의 주사위로 한 변의 길이가 n인 정육면체를 만든다.
# 보이는 다섯면의 숫자의 합의 최소를 구하라
#   D
# E A B F
#   C       주사위는 이렇게 생겼다.
# 주사위에 들어갈 숫자가 주어진다.

n = int(input())
num = list(map(int,input().split(' ')))

main_num = min(num)

two_num = 1000000000
for i in range(6):
    for j in range(i+1,6):
        if i+j == 5: continue
        if num[i]+num[j] < two_num:
            two_num = num[i]+num[j]

three_num = min(num[0],num[5])+min(num[1],num[4])+min(num[2],num[3])

if n >= 3:
    ans = three_num*4 + two_num*(n-1)*4 + two_num*(n-2)*4 + main_num*(n-2)*(n-2) + main_num*(n-1)*(n-2)*4
    print(ans)
elif n == 1:
    print(sum(num)-max(num))
elif n == 2:
    ans = three_num*4 + two_num*4
    print(ans)