# -*- coding: utf-8 -*-
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return

def solution(phone_book):

    dic_phone = {}
    for el in phone_book:
        try:
            dic_phone[el[0]].append(el)
            for i in range(0,len(dic_phone[el[0]])-1):
                if dic_phone[el[0]][i] in el or el in dic_phone[el[0]][i]:
                    return False
        except:
            dic_phone[el[0]] = [el]
    return True

phone_book = ["88","12","123","1235","567"]
print(solution(phone_book))