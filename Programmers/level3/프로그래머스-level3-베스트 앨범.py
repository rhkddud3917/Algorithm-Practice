# -*- coding: utf-8 -*-
# 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.

import heapq

def solution(genres, plays):
    answer = []

    # res_dict 라는 딕셔너리에 장르를 키로 정보를 저장한다.
    # 키에 해당하는 벨류의 첫 번째 값은 해당 장르의 총 재생 횟수를 계속 더해나가는 것이고
    # 두번째 값은 최대 heap으로 해당 노래의 재생횟수와 고유번호를 저장한다.
    res_dict = {}
    for i in range(0,len(genres)):
        try:
            res_dict[genres[i]][0] += plays[i]
            heapq.heappush(res_dict[genres[i]][1],(-plays[i],plays[i],i))
        except:
            res_dict[genres[i]] = [plays[i],[]]
            heapq.heappush(res_dict[genres[i]][1],(-plays[i],plays[i],i))

    # 위에서 만든 딕셔너리에서 장르의 재생횟수가 많은 순으로 정렬을 한다.
    genres_list = []
    for el in res_dict.keys():
        genres_list.append([res_dict[el][0],el])
    genres_list.sort(reverse=True)

    # 재생횟수가 많은 순으로 정렬이 된 장르의 리스트를 차례로 읽어가며
    # 해당 장르에 대한 정보를 딕셔너리에서 읽는다.
    # 최대 힙으로 구성되어 있으므로 pop을 함으르서 장르안에서의 재생횟수가 많은 노래를 뽑아서 answer에 저장한다.
    for el in genres_list:
        for i in range(0,min(len(res_dict[el[1]][1]),2)):
            answer.append(heapq.heappop(res_dict[el[1]][1])[2])

    return answer

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
print(solution(genres,plays))