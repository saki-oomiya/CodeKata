#!/usr/bin/python
# -*- coding: utf-8 -*-

num = input("円盤の枚数を入力してください>>> ")

if num.isdigit() == False:
    print("入力された文字は数字ではありません。数字を入力してください。")
    exit()

n = int(num)
start = "A"
work = "B"
end = "C"
cnt = 0

def hanoi(n,start,end,work):
    global cnt
    if n > 0:
        hanoi(n-1,start,work,end)
        print(n,"番目の円盤を",start,"から",end,"へ移動させます。")
        cnt += 1
        hanoi(n-1,work,end,start)

hanoi(n,start,end,work)
print("すべての円盤を移動させるのに",cnt,"回かかりました。")