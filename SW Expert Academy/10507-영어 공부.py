T = int(input())
for test_case in range(1, T + 1):
    num,eng = map(int,input().split(' '))
    date = list(map(int,input().split(' ')))
    start = 0
    end = 1
    leng = 0
    max_leng = 0
    eng_point = eng

    while True:
        if end == num:
            leng = date[end-1] - date[start] + 1 + eng_point
            if max_leng < leng: max_leng = leng
            break

        emp = date[end] - date[end-1] -1
        if emp > eng:
            leng = date[end - 1] - date[start] + 1 + eng_point
            if max_leng < leng: max_leng = leng
            start = end
            end = end + 1
            eng_point = eng
        else:
            if emp <= eng_point:
                end = end + 1
                eng_point = eng_point - emp
                leng = date[end-1] - date[start] + 1
                if max_leng < leng: max_leng = leng
            else:
                leng = date[end-1] - date[start] + 1 + eng_point
                if max_leng < leng: max_leng = leng
                start = start + 1
                eng_point = eng_point + date[start] - date[start-1] - 1
                leng = date[end-1] - date[start] + 1

    print("#"+str(test_case),max_leng)



