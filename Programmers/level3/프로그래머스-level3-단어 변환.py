# -*- coding: utf-8 -*-
# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다.
# 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return
# 변환할 수 없는 경우에는 0를 return

# 단어 끼리 서로 다른 알파벳이 하나 일 경우에만 True를 리턴하는 함수
def compa(a,b):
    c = 0
    for i in range(0,len(a)):
        if a[i] != b[i]: c += 1
        if c >= 2: return False
    if c == 1:
        return True
    return False

# bfs를 수행하는 함수 queue를 이용했다.
def bfs(begin,target,words):

    check = [0] * (len(words))
    myqueue = []

    myqueue.append(-1)
    count = 0

    while len(myqueue) != 0:
        l = len(myqueue)
        for i in range(0,l):
            x = myqueue.pop(0)
            for el in range(0,len(words)):
                if x == -1:
                    if check[el] == 0 and compa(begin, words[el]):
                        check[el] = count + 1
                        myqueue.append(el)
                else:
                    if check[el] == 0 and compa(words[x],words[el]):
                        check[el] = count + 1
                        myqueue.append(el)
        count += 1

    index = 0
    for i in range(0,len(words)):
        if target == words[i]:
            index = i
            break
    return check[index]


def solution(begin, target, words):


    if target not in words: return 0

    # bfs 를 통해 각 단어 노드에 대해서 begin과의 최소 거리를 구한다.
    return bfs(begin,target,words)


begin = "hit"
target = "cog"
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
print(solution(begin,target,words))