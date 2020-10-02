# 건물은 건물 규칙에 따라 특정 건물들을 지엇을 경우 그 건물을 지을 수 있을 수 있다.
# 건물의 수, 건물을 짓는데 걸리는 시간, 건물 규칙이 주어질때
# 원하는 건물을 짓는데까지 최소시간 구하기

import sys

# 전체 적인 알고리즘은 각 건물을 짓기 위한 필요 건물들의 목록을 저장을 하였고
# 건물을 짓기 위해 필요한 시간은 해당 건물을 짓기위한 건물들의 목록을 탐색하여 가장 오래 걸리는 건물을 선택하고 거기에 해당 건물을 짓는 시간을 더했다.
# 목표 건물로 부터 재귀함수를 통해 거꾸로 접근하여 답을 구했다.
# 시간 초과를 줄이기 위해 각 건물의 최소 짓는 시간을 최초 계산할 때 저장하였고
# 후에 이 건물에 대한 정보가 쓰일 때 다시 계산을 하지 않고 저장된 값을 사용했다.
def find(x):

    try:
        dict[x]
    except:
        time_dict[x] = time[x]
        return time[x]
    longest = 0
    try:
        return time_dict[x]
    except:
        for el in dict[x]:
            try:
                if longest < time_dict[el]:
                    longest = time_dict[el]
            except:
                if longest < find(el):
                    longest = find(el)
        longest = longest + time[x]
        time_dict[x] = longest
        return longest

test = int(sys.stdin.readline())

for t in range(test):
    building,rules = map(int,sys.stdin.readline().split(' '))

    time = list(map(int,sys.stdin.readline().split(' ')))
    dict = {}
    time_dict = {}
    for r in range(rules):
        s,e = list(map(int,sys.stdin.readline().split(' ')))
        try:
            dict[e-1].append(s-1)
        except:
            dict[e-1] = [s-1]
    target = int(sys.stdin.readline())
    print(find(target-1))