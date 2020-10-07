# 감염된 컴퓨터와 연결된 모든 컴퓨터는 감염된다.
# 감염되는 컴퓨터의 수 출력

n = int(input())
m = int(input())

dict = {}

for i in range(m):
    s,e = list(map(int,input().split()))
    try:
        dict[s-1].append(e-1)
    except:
        dict[s-1] = [e-1]
    try:
        dict[e-1].append(s-1)
    except:
        dict[e-1] = [s-1]

state = list(range(n))
check = [0]*n

temp = list(dict.keys())
temp.sort()

def dfs(el,val):
    for e in dict[el]:
        if check[e] == 0:
            state[e] = val
            check[e] = 1
            dfs(e,val)

for el in temp:
    if check[el] == 0:
        state[el] = el
        check[el] = 1
        dfs(el,el)

count = 0
for el in state:
    if el == 0:
        count += 1

print(count-1)

