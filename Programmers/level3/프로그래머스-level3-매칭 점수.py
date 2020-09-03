# -*- coding: utf-8 -*-

import re

def solution(word, pages):
    total = []
    k = 0
    for el in pages:
        # 태그 별로 나눔
        temp = el.split(">")

        address= []
        # 페이지 주소 찾기
        for i in range(0,len(temp)):
            if("https://" in temp[i]):
                if("<meta" in temp[i] or "<a href" in temp[i]):
                    address.append(temp[i])

        for i in range(0, len(address)):
            temp2 = address[i].split(" ")
            for t in range(0,len(temp2)):
                if("https://" in temp2[t]):
                    address[i] = temp2[t]
            a = list(address[i])
            for j in range(0, len(a)):
                if (a[j] == '"' or a[j] == "'"):
                    point = j
                    break
            address[i] = address[i][point + 1:]
            a = list(address[i])
            for j in range(0, len(a)):
                if (a[j] == '"' or a[j] == "'"):
                    point = j
            address[i] = address[i][:point]


        # 단어 등장 횟수
        count = 0
        for el3 in temp:
            tmp = el3.split(" ")
            for y in tmp:
                temp2 = re.split('[^a-zA-Z]',y)
                for el5 in temp2:
                    if(word.lower() == el5.lower()):
                        count += 1

        # 외부 링크 수
        linknum = len(address)-1

        outaddress = []
        if(len(address)>=2):
            for el in range(1,len(address)):
                outaddress.append(address[el])
        else:
            outaddress = []

        # 인덱스, 주소이름, 단어등장 수, 외부링크 수, 외부링크 주소들, 점수
        total.append([k, address[0], count, linknum, outaddress, count])
        k += 1

    for i in range(0,len(total)):
        main = total[i][1]
        for el2 in total:
            for ele in el2[4]:
                if(main == ele):
                    total[i][5] += el2[2] / el2[3]

    print(total)

    total = sorted(total, key = lambda x: (-x[5], x[0]))
    answer = total[0][0]

    return answer