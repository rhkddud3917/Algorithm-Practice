# N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성
# 단어를 숫자에 대응시켜야 한다.

n = int(input())

dict = {}

store = []
for _ in range(n):
    s = list(input())
    store.append(s)
    l = len(s)
    for i in range(l):
        try:
            dict[s[i]] += 10**(l-i)
        except:
            dict[s[i]] = 10**(l-i)

item = []
for k,v in dict.items():
    item.append([k,v])

item.sort(key = lambda x: -x[1])

for i in range(len(item)):
    dict[item[i][0]] = str(9-i)

answer = 0
for el in store:
    for i in range(len(el)):
        el[i] = dict[el[i]]
    temp = ''.join(el)
    answer += int(temp)

print(answer)
