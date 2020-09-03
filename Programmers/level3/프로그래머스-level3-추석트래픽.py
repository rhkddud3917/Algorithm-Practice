# -*- coding: utf-8 -*-
# 초당 최대 처리량은 요청의 응답 완료 여부에 관계없이 임의 시간부터 1초(=1,000밀리초)간 처리하는 요청의 최대 개수를 의미한다.
# solution 함수에서는 로그 데이터 lines 배열에 대해 초당 최대 처리량을 리턴한다.
# 각 로그 문자열마다 요청에 대한 응답완료시간 S와 처리시간 T가 공백으로 구분되어 있다.
# 로그 문자열 2016-09-15 03:10:33.020 0.011s은
# 2016년 9월 15일 오전 3시 10분 **33.010초**부터 2016년 9월 15일 오전 3시 10분 **33.020초**까지 **0.011초** 동안 처리된 요청을 의미한다.
# 처리시간은 시작시간과 끝시간을 포함
# 서버에는 타임아웃이 3초로 적용되어 있기 때문에 처리시간은 0.001 ≦ T ≦ 3.000이다.

def solution(lines):

    newline=[]

    # 주어진 응답 처리 완료시간과 처리 시간을 처리시작시간과 처리 완료시간으로 정리한다.
    for i in lines:
        first = i.split(" ")[1:]
        second = first[0].split(":")
        third = first[1][:-1]
        reardata = float(second[0])*3600 + float(second[1])*60 + float(second[2])
        frontdata = (reardata - float(third)+0.001)
        frontdata = float(format(frontdata, ".3f"))
        newline.append((frontdata, reardata))

    newline = sorted(newline)

    # 초당 최대 처리량의 시작 시간의 후보는 응답의 처리시작시간, 처리 완료시간들이다.
    candidate = []
    for el in newline:
        for el2 in el:
            candidate.append(el2)
    candidate.sort()

    # 후보들 중에서 초당 최대 처리량이 가장 높은 것의 처리량을 계산한다.
    ans = 0
    for c in candidate:
        count = 0
        for el in newline:
            if c + 1 <= el[0]: continue
            else:
                if (c >= el[0] and c <= el[1]) or\
                        (c+1 > el[0] and c+1 < el[1]) or\
                        (c < el[0] and c+1 > el[1]):
                    count += 1
        if ans < count: ans = count

    return ans

lines =  ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
print(solution(lines))
