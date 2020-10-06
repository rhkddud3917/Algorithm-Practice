# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 정점 번호는 1번부터 N번까지이다.

n, m, start = list(map(int,input().split(' ')))

dict = {}
check = [0]*(n+1)

for i in range(m):
    s,e = list(map(int,input().split(' ')))
    try:
        dict[s].append(e)
    except:
        dict[s] = [e]
    try:
        dict[e].append(s)
    except:
        dict[e] = [s]

answer1 = []
answer2 = []

def dfs(i):
    answer1.append(i)
    check[i] = 1
    try:
        target = dict[i]
        target.sort()
    except:
        target = []
    for el in target:
        if check[el] == 1: continue
        dfs(el)
    return

dfs(start)
answer1 = list(map(str,answer1))
print(' '.join(answer1))

check = [0]*(n+1)

def bfs(i):
    my_queue = []
    my_queue.append(i)

    while len(my_queue) != 0:
        x = my_queue.pop(0)
        if check[x] == 0:
            answer2.append(x)
            check[x] = 1
        try:
            target = dict[x]
            target.sort()
        except:
            target = []
        for el in target:
            if check[el] == 1: continue
            my_queue.append(el)

bfs(start)

answer2 = list(map(str,answer2))
print(' '.join(answer2))
