T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    name = {}
    for _ in range(num):
        word = input()
        l = len(word)
        try:
            for i in range(len(name[l])):
                if name[l][i] > word:
                    name[l].insert(i,word)
                    break
                elif name[l][i] == word:
                    break
            else:
                name[l].append(word)
        except:
            name[l] = [word]
    temp = list(name.keys())
    temp.sort()
    print('#'+str(test_case))
    for el in temp:
        for e in name[el]:
            print(e)


