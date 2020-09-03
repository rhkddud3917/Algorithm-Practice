# -*- coding: utf-8 -*-
# m 은 기억하고 있는 멜로디
# musicinfos 는 시작, 끝 시간, 제목 악보
# 재생되는 시간에 따라 잘릴수도 계속 반복될수도 있음
# 찾으려는 음악제목 출력
# 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
# 조건이 일치하는 음악이 없을 때에는 `(None)`을 반환한다.

# KMP 알고리즘 이용
# get_prefix_table과 strstr 함수는 kmp 알고리즘을 구현한 함수
# 문자열비교를 통해 해당 패턴이 있으면 시작 인덱스를 없으면 -1 반환
def get_prefix_table(needle):
    prefix_set = set()
    n = len(needle)
    prefix_table = [0]*n
    delimeter = 1
    while(delimeter<n):
        prefix_set.add(needle[:delimeter])
        j = 1
        while(j<delimeter+1):
            if needle[j:delimeter+1] in prefix_set:
                prefix_table[delimeter] = delimeter - j + 1
                break
            j += 1
        delimeter += 1
    return prefix_table

def strstr(haystack, needle):
    # m: denoting the position within S where the prospective match for W begins
    # i: denoting the index of the currently considered character in W.
    haystack_len = len(haystack)
    needle_len = len(needle)
    if (needle_len > haystack_len) or (not haystack_len) or (not needle_len):
        return -1
    prefix_table = get_prefix_table(needle)
    m = i = 0
    while((i<needle_len) and (m<haystack_len)):
        if haystack[m] == needle[i]:
            i += 1
            m += 1
        else:
            if i != 0:
                i = prefix_table[i-1]
            else:
                m += 1
    if i==needle_len and haystack[m-1] == needle[i-1]:
        return m - needle_len
    else:
        return -1

def solution(m, musicinfos):

    res = []

    # 멜로디에서 # 이 붙은 것들을 처리해 준다. 하나의 알파벳으로 나타내기 위해 다른 알파벳을 사용한다.
    m = list(m)
    mel = []
    for el in m:
        if el == '#':
            if mel[len(mel) - 1] == 'C': mel[len(mel) - 1] = 'X'
            if mel[len(mel) - 1] == 'D': mel[len(mel) - 1] = 'Y'
            if mel[len(mel) - 1] == 'F': mel[len(mel) - 1] = 'Z'
            if mel[len(mel) - 1] == 'G': mel[len(mel) - 1] = 'S'
            if mel[len(mel) - 1] == 'A': mel[len(mel) - 1] = 'T'
        else:
            mel.append(el)

    count = 0
    for el in musicinfos:
        # 재생 시간 계산
        el = el.split(',')
        start = el[0].split(':')
        start = int(start[0]) * 60 + int(start[1])
        end = el[1].split(':')
        end = int(end[0]) * 60 + int(end[1])
        time = int(end) - int(start)

        # 재생되는 악보에서 멜로디와 마찬가지로 # 문자 없애기
        p = list(el[3])
        played = []
        for e in p:
            if e == '#':
                if played[len(played)-1] == 'C': played[len(played)-1] = 'X'
                if played[len(played) - 1] == 'D': played[len(played)-1] = 'Y'
                if played[len(played) - 1] == 'F': played[len(played)-1] = 'Z'
                if played[len(played) - 1] == 'G': played[len(played)-1] = 'S'
                if played[len(played) - 1] == 'A': played[len(played)-1] = 'T'
            else:
                played.append(e)

        # 재생시간에 맞추어 재생된 악보 생성
        play = []
        for i in range(0,time):
            play.append(played[i % len(played)])

        # KMP 문자열 비교 알고리즘을 통해 멜로디가 악보에 존재하는지 확인
        t = strstr(''.join(play),''.join(mel))
        if t != -1:
            res.append([time,el[2],count])
        count += 1

    # 예외 처리 후 문제 조건에 맞추어 출력
    if len(res) == 0: return "(None)"
    elif len(res) == 1: return res[0][1]
    else:
        res = sorted(res, key=lambda x: (-x[0],x[2]))
        return res[0][1]

m = "ABC"
musicinfos = ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']
print(solution(m,musicinfos))