#!/usr/bin/python
# -*- coding: utf-8 -*-

column = int(input("行列の列数を入力してください>>> "))
line = int(input("行列の行数を入力してください>>> "))

col = [[] for i in range(column)]
row = [[] for j in range(line)]

for n in range(1, column + 1):
    for m in range(1, line + 1):
        col[n - 1].append(input(str(n) + "行目の" + str(m) + "列番目を入力してください。"))

for m in range(1, line + 1):
    for n in range(1, column + 1):
        row[m - 1].append(0)

for a in range(column):
    print(col[a])

for b in range(column):
    for c in range(line):
        row[c][b] = col[b][c]

print("入力された値の転置行列は")
for d in range(line):
    print(row[d])
print("です。")