# -*- coding: utf-8 -*-
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
# 단어에 포함되어 있는 a의 개수, b의 개수, …, z의 개수를 공백으로 구분해서 출력한다.

s = input()

temp = 'abcdefghijklmnopqrstuvwxyz'
string_dic = {}
for i in range(0,len(temp)):
    string_dic[temp[i]] = 0

for i in range(0,len(s)):
    string_dic[s[i]] += 1

answer = ''
for i in range(0,len(temp)):
    answer = answer + str(string_dic[temp[i]]) + ' '

print(answer[:-1])

