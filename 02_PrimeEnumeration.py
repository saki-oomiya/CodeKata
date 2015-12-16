#!/usr/bin/python
# -*- coding: utf-8 -*-

num = input("数字を入力してください>>> ")

if num.isdigit() == False:
    print("入力された文字は数字ではありません。数字を入力してください。")
    exit()

no = int(num)
flg = 0
s = ""

for n in range(1,no+1):
    g = 0
    for m in range(1,n+1):
        if(n%m==0):
            g += 1
    if(g==2):
        s += str(n)+","

s = s[:-1]
print(no,"までの数字で素数であるのは",s,"です。")

