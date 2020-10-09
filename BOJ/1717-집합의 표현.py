# 합집합은 0 a b의 형태로 입력이 주어진다. 이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다.
# 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다.
# 이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다.
# 앞이 1인 연산에 대해서 YES, NO를 차례대로 출력
# 초기에 n+1개의 집합이 있다.

from collections import deque

n,m = map(int,input().split())

parent = []
for i in range(n+1):
    parent.append(i)

def get_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = get_parent(parent[x])
        return parent[x]

def union(x,y):
    p = get_parent(x)
    q = get_parent(y)

    if p != q:
        if p < q:
            parent[q] = p
        elif p > q:
            parent[p] = q

for i in range(m):
    a,b,c = map(int,input().split())

    if a == 0:
        union(b,c)

    elif a == 1:
        if get_parent(b) == get_parent(c): print("YES")
        else: print("NO")
