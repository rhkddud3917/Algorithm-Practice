def dfs(x,val):
    for el in know_dict[x]:
        if check[el] == 0:
            state[el] = val
            check[el] = 1
            dfs(el,val)

T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int,input().split(' '))

    know_dict = {}
    for _ in range(m):
        a,b = map(int,input().split(' '))
        try:
            know_dict[a-1].append(b-1)
        except:
            know_dict[a-1] = [b-1]
        try:
            know_dict[b-1].append(a-1)
        except:
            know_dict[b-1] = [a-1]

    state = []
    check = []
    for i in range(n):
        state.append(i)
        check.append(0)

    temp = list(know_dict.keys())
    temp.sort()

    for el in temp:
        if check[el] == 0:
            state[el] = el
            check[el] = 1
            dfs(el,el)

    print('#'+str(test_case),len(set(state)))