# -*- coding: utf-8 -*-
# 입력된 도시이름 배열을 순서대로 처리할 때, 총 실행시간을 출력한다.
# 캐시 히트는 1 미스는 5
# 캐시 교체 알고리즘은 LRU

def solution(cacheSize, cities):
    answer = 0
    cache = []
    # 캐시사이즈가 0 인경우
    if cacheSize == 0: return len(cities)*5

    # 캐시 만들기 [도시이름, 이용된 인덱스]
    for i in range(0,cacheSize):
        cache.append(['0',-1])

    for i in range(0,len(cities)):
        hit = 0
        for j in range(0,len(cache)):
            # 캐시 히트
            if cities[i].upper() == cache[j][0]:
                answer += 1
                cache[j][1] = i
                hit = 1
                break
        if hit == 0:
            # 캐시 미스
            # 캐시 교체 해야함
            mini = 1000000
            index = 0
            # LRU 캐시 교체 알고리즘
            for j in range(0,len(cache)):
                if cache[j][0] == '0':
                    index = j
                    break
                if mini > cache[j][1]:
                    mini = cache[j][1]
                    index = j
            cache[index][0] = cities[i].upper()
            cache[index][1] = i
            answer += 5
        #print(cache)
    return answer

cacheSize = 3
cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
print(solution(cacheSize,cities))
