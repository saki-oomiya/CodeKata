#!/usr/bin/python
# -*- coding: utf-8 -*-

num = input("西暦を入力してください>>> ")

if num.isdigit() == False:
    print("入力された文字は数字ではありません。数字を入力してください。")
    exit()

year = int(num)

if(year % 400 == 0):
    print(year,"年は閏年です。")

elif(year % 100 ==0):
    print(year,"年は閏年ではありません。")

elif(year % 4 ==0):
    print(year,"年は閏年です。")

else:
    print(year,"年は閏年ではありません。")






