# 두 좌표가 주어지고 두 좌표로 부터 목적지의 거리가 주어질 때 목적지가 존재할 수 있는 좌표의 수 반환
# 한 줄에 x1, y1, r1, x2, y2, r2가 주어진다.
# 위치의 개수가 무한대일 경우에는 -1을 출력

num = int(input())

for test in range(num):
    s = list(map(int,input().split(' ')))
    x1,y1,r1,x2,y2,r2 = s[0],s[1],s[2],s[3],s[4],s[5]

    dist = (x2-x1)**2+(y2-y1)**2
    if x1 == x2 and y1 == y2:
        if r1 == r2: print(-1)
        elif r1 != r2: print(0)
    else:
        if (r1-r2)**2 < dist and dist < (r1 + r2)**2: print(2)
        elif dist == (r1-r2)**2 or dist == (r1 + r2)**2: print(1)
        else: print(0)

# 예외라고 해야 할지는 모르겠으나
# 모든 경우에 대해서 처리하는데 시간이 걸렸다.
# 한 원이 다른 원 안에 존재하는 경우를 생각하는 것이 어려웠다.