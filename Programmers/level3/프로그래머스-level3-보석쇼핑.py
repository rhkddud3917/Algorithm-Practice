# -*- coding: utf-8 -*-
# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매하는 규칙을 따른다.
# 진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems가 매개변수로 주어집니다. 이때 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 return
# 가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return 하도록 하며,
# 만약 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return

def solution(gems):
    answer = [0,0]

    # 보석의 종류 별로 딕셔너리를 만든다.
    gem_dict = {}
    gem_set = set(gems)
    for el in gem_set:
        gem_dict[el] = 0

    leng = len(gems)
    check = 0
    start = 0
    end = 0

    # 처음 부터 한칸씩 전진하면서 구간에 가지고 있는 보석의 수를 딕셔너리에 저장한다.
    # 모든 보석을 가지고 있으면 맨 앞부터 하나씩 빼보면서 빼도 모든 보석이 존재하는지 확인을 한다.
    # 짧은 구간이 나올 때마다 답을 업데이트한다.
    for i in range(0,len(gems)):
        if gem_dict[gems[i]] == 0:
            check += 1
        gem_dict[gems[i]] += 1

        if check == len(gem_set):
            end = i
            while gem_dict[gems[start]] >= 2:
                gem_dict[gems[start]] -= 1
                start += 1
            if leng > end-start:
                answer[0] = start
                answer[1] = end
                leng = end-start

    return [answer[0]+1,answer[1]+1]

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))