# -*- coding: utf-8 -*-
# 사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때,
# 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return

def solution(n, words):
    word_dic = {}
    res = -1

    # 이미 나온 단어를 효율적을 서치 하기 위해 dictionary 사용
    for i in range(0,len(words)):
        if i != 0:
            # 끝말잇기를 제대로 했는지 확인
            if words[i][0] != words[i-1][-1]:
                res = i
                break
        # 딕션어리에 넣어보고 되면 이미 있는 단어인지 확인
        try:
            if words[i] in word_dic[words[i][0]]:
                x = True
            else: x = False
            word_dic[words[i][0]].append(words[i])
        # 해당 알파벳으로 시작하는 단어가 처음 나온 것이면 딕션어리에 키 벨류 추가
        except:
            word_dic[words[i][0]] = [words[i]]
            x = False
        if x == True:
            res = i
            break
    # 정상적인 끝말잇기면 [0,0] 반환
    if res == -1: return [0,0]
    answer = [res%n+1, res//n+1]

    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n,words))