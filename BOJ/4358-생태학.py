# 주어진 각 종의 이름을 사전순으로 출력하고, 그 종이 차지하는 비율을 백분율로 소수점 4째자리까지 함께 출력한다.
import sys

dict = {}

count = 0
while True:
    s = sys.stdin.readline().rstrip()
    if s == '\n': break
    if s == '': break
    count += 1
    try:
        dict[s] += 1
    except:
        dict[s] = 1

x = list(dict.keys())
x.sort()

for el in x:
    print("%s %.4f"%(el,dict[el]/count*100))
