# 은하수 지도, 출발점, 도착점이 주어졌을 때 어린 왕자에게 필요한 최소의 행성계 진입/이탈 횟수를 구하는 프로그램을 작성
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
# 그 다음 줄부터 각각의 테스트케이스에 대해 첫째 줄에 출발점 (x1, y1)과 도착점 (x2, y2)이 주어진다.
# 두 번째 줄에는 행성계의 개수 n이 주어지며, 세 번째 줄부터 n줄에 걸쳐 행성계의 중점과 반지름 (cx, cy, r)이 주어진다.

test = int(input())


for t in range(test):
    s = list(map(int, input().split(' ')))
    x1, y1, x2, y2 = s[0], s[1], s[2], s[3]
    count = 0
    num = int(input())
    for n in range(num):
        p = list(map(int,input().split(' ')))
        x,y,r = p[0],p[1],p[2]
        dist1 = (x1-x)**2 + (y1-y)**2
        dist2 = (x2-x)**2 + (y2-y)**2
        if dist1 < r**2 and dist2 > r**2: count += 1
        elif dist2 < r**2 and dist1 > r**2: count += 1
    print(count)