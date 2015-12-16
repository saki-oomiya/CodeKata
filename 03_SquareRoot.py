#!/usr/bin/python
# -*- coding: utf-8 -*-

num = input("数字を入力してください>>> ")

if num.isdigit() == False:
    print("入力された文字は数字ではありません。数字を入力してください。")
    exit()

no = int(num)
n = no / 2.0
last_n = 0.0

while n != last_n:
    last_n = n
    n = (n + no / n) / 2.0

print(no,"の平方根は",n,"です。")