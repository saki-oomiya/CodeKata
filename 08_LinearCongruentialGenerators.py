#!/usr/bin/python
# -*- coding: utf-8 -*-

M = 2 ^ 16
A = 997
B = 1
X = 12345
n = 100
list = []

for i in range(n):
    X = (A * X + B) % M
    list.append(round(float(X) / M, 4))

print(list)
print("平均=",round(sum(list) / n, 4))