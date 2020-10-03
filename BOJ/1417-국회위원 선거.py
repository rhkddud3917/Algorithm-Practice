# 현재 형택구에 나온 국회의원 후보는 N명이다. 다솜이는 이 기계를 이용해서 그 마을의 주민 M명의 마음을 모두 읽었다.
# 돈으로 매수한 사람은 반드시 다솜이를 찍는다고 가정한다.
# 다솜이가 매수해야하는 사람의 최솟값을 출력
# 다솜이는 기호 1번이다.

num = int(input())
dasom = int(input())
candi = []
answer = 0

for i in range(num-1):
    candi.append(int(input()))

while len(candi) != 0 and dasom <= max(candi):

    index = 0
    big = 0
    for i in range(len(candi)):
        if candi[i] > big:
            big = candi[i]
            index = i

    candi[index] -= 1
    dasom += 1
    answer += 1

print(answer)
