# -*- coding: utf-8 -*-
# 1 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
# 2 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
# 3 w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
# 4 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
# 5 단계 2로 돌아간다.
# 예시
# 현재 사전에는 KAKAO의 첫 글자 K는 등록되어 있으나, 두 번째 글자까지인 KA는 없으므로, 첫 글자 K에 해당하는 색인 번호 11을 출력하고,
# 다음 글자인 A를 포함한 KA를 사전에 27 번째로 등록한다.
# 두 번째 글자 A는 사전에 있으나, 세 번째 글자까지인 AK는 사전에 없으므로, A의 색인 번호 1을 출력하고, AK를 사전에 28 번째로 등록한다.
# 세 번째 글자에서 시작하는 KA가 사전에 있으므로, KA에 해당하는 색인 번호 27을 출력하고, 다음 글자 O를 포함한 KAO를 29 번째로 등록한다.
# 마지막으로 처리되지 않은 글자 O에 해당하는 색인 번호 15를 출력한다.
# 문자열을 입력받았을때 문자열을 압축한 후의 색인 번호를 배열로 반환

def solution(msg):
    answer = []

    # 알파벳 딕셔너리 만들기
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word_dic = {}
    for i in range(0,len(alpha)):
        word_dic[alpha[i]] = i+1

    index = 0
    while True:
        count = 0
        # 최대한 긴 글자가 딕셔너리에 있는지 확인
        while True:
            if index+count > len(msg):
                break
            if msg[index:index+count+1] not in word_dic.keys():
                break
            else: count += 1
        # 기존에 있던 문자열보다 하나 긴 문자열 딕셔너리에 추가 및 결과 값 리턴
        answer.append(word_dic[msg[index:index+count]])
        word_dic[msg[index:index+count+1]] = len(word_dic)+1
        index += count
        if index >= len(msg): break
    return answer

msg = 'ABABABABABABABAB'
print(solution(msg))