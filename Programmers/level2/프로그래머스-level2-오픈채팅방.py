# -*- coding: utf-8 -*-
# 닉네임 들어왔습니다, 닉네임 나갔습니다 출력해야함
# 닉네임을 변경하면 그동안 있던 입, 출 메시지 닉네임 다 바뀜
# 중복 닉네임 허용
# 닉네임 변경 결과를 반영한 입,출 메시지 목록 출력
# Enter [유저 아이디] [닉네임] / Leave [유저 아이디] / Change [유저 아이디] [닉네임]
# [닉네임]님이 들어왔습니다. / [닉네임]님이 나갔습니다.

def solution(record):
    answer = []
    semi = []
    # 아이디 : 닉네임 딕셔너리 만듦
    id_dic = {}

    # enter, change일때만 딕셔너리 업데이트
    # enter, leave 일때만 메시지 업데이트
    for re in record:
        re = re.split(' ')
        if re[0][0] == "E":
            semi.append([re[1], '님이 들어왔습니다.'])
            id_dic[re[1]] = re[2]
        elif re[0][0] == "L":
            semi.append([re[1], '님이 나갔습니다.'])
        else:
            id_dic[re[1]] = re[2]

    for el in semi:
        answer.append(id_dic[el[0]]+el[1])
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
