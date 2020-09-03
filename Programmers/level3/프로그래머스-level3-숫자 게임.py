# -*- coding: utf-8 -*-

def solution(a, b):
    # b 를 오름차순으로 정렬
    b = sorted(b)
    a = sorted(a)
    bmax = max(b)
    answer = 0
    k = 0
    b_index = 0

    # 길이가 1일때
    if(len(a) == 1):
        if(a[0] < b[0]):
            return 1
        else:
            return 0

    while(k <= len(a)-1):
        check = 0
        if a[k] >= bmax:
            del b[0]
            check = 1
        if(check == 0):
            for i in range(b_index,len(b)):
                if(a[k] < b[i]):
                    answer += 1
                    temp = b[i]
                    del b[i]
                    if(bmax == temp):
                        if(len(b)>0):
                            bmax = max(b)
                    break
            b_index = i
        k += 1



    return answer