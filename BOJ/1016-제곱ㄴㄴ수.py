# 어떤 수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 제곱ㄴㄴ수라고 한다. 제곱수는 정수의 제곱이다.
# min과 max가 주어지면, min과 max를 포함한 사이에 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

mini, maxi = list(map(int,input().split(' ')))

start = 2
end = int(maxi**0.5)
count = maxi-mini+1

a = [False,False] + [True]*(end-1)
primes = []

for i in range(2,end+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, end+1, i):
        a[j] = False

for el in primes:
    x = maxi//(el**2)
    y = mini//(el**2)
    if mini % (el**2) != 0: y += 1
    y = max(y,0)
    temp = x - y + 1
    count -= temp

print(count)
