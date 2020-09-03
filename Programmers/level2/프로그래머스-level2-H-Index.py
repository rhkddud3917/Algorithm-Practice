# -*- coding: utf-8 -*-
# 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
# 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    min_v = citations[len(citations)-1]
    max_v = citations[0]

    if len(citations) == 1:
        if citations[0] == 1 or citations[0] == 0:
            return 1
        else:
            return 0

    max = [0,0]
    for i in range(0,max_v+1):
        use = 0
        for el in range(0,len(citations)):
            if citations[el] < i:
                break
            else:
                use+=1
        if i <= use:
            max[0] = use
            max[1] = i

    return max[1]

citations = [22,42]
print(solution(citations))