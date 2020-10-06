# 지민이는 N쪽인 책이 한권 있다. 첫 페이지는 1쪽이고, 마지막 페이지는 N쪽이다. 각 숫자가 모두 몇 번이 나오는지 출력하는 프로그램을 작성하시오.
# 첫째 줄에 0이 총 몇 번 나오는지, 1이 총 몇 번 나오는지, ..., 9가 총 몇 번 나오는지를 출력한다.

num = input()
l = len(num)

answer = [0]*10

if l == 1:
    x = int(num[0])
    for i in range(1,x+1):
        answer[i] += 1

else:
    for i in range(l):
        if i == 0:
            x = int(num[i])
            for j in range(1,x):
                answer[j] += 10**(l-1)
            back = int(num[i+1:])
            answer[x] += back+1

        elif i == l-1:
            x = int(num[i])
            front = int(num[:i])
            for j in range(10):
                answer[j] += front
            for j in range(x+1):
                answer[j] += 1

        else:
            x = int(num[i])
            front = int(num[:i])
            back = int(num[i+1:])
            for j in range(1,10):
                answer[j] += front*10**(l-1-i)
            answer[0] += (front-1)*10**(l-1-i)
            for j in range(x):
                answer[j] += 10**(l-1-i)
            answer[x] += back+1

    answer[0] -= 1

answer = list(map(str,answer))
print(' '.join(answer))


