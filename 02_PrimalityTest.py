#!/usr/bin/python
# -*- coding: utf-8 -*-

num = input("数字を入力してください>>> ")

if num.isdigit() == False:
    print("入力された文字は数字ではありません。数字を入力してください。")
    exit()

no = int(num)
flg = 0
s = ""

for i in range(2,no):
    if(no%i==0):
        flg = 1
        s += str(i)+","

if(flg==0):
    print(no,"は素数です。")
else:
    s = s[:-1]
    print(no,"は",s,"で割り切ることができるため、素数ではありません。")