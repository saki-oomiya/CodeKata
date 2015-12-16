#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

num = input("数当てゲームです。数値を入力してください>>> ")

if num.isdigit() == False:
    print("入力された文字は数字ではありません。数字を入力してください。")
    exit()

no = int(num)
answer = round(random.uniform(1, 100))

while(no != answer):
    if(no > answer):
        print("入力された数値は答えの数よりも大きいです。")
        no = int(input("次の数値を入力してください。"))
    else:
        print("入力された数値は答えの数よりも小さいです。")
        no = int(input("次の数値を入力してください。"))

print("正解です！")
print("答えの数は",answer,"でした。")






