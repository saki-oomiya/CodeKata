#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import shuffle, choice
from itertools import count
from collections import defaultdict

with open("CapVerses.txt") as file:
    dic = list(set(file.read().strip().split('\n')))

first = [word[0] for word in dic]
use = defaultdict(int)
players = [ "貴方", "私" ]

shuffle(players)
startswith = None

for i in count(1):
    if players[i % len(players)] == "貴方":
        if startswith == None:
            startswith = choice(first)

        print(i,":貴方の番です。",startswith,":")
        answer = input()

        while not (answer.startswith(startswith) and answer in dic):
            if not answer.startswith(startswith):
                print(startswith,"で始まっていません。")
            else:
                print("辞書にありません。")

            print(i,":貴方の番です。",startswith,":")
            answer = input()

        if answer in dic:
            if answer in use:
                print(answer,"は",use[answer],"回目に",players[use[answer]%len(players)],"が使用しています。私の勝ちです。")
                break

            startswith = answer[-1]
            use[answer] = i

    else:
        if startswith == None:
            reply = choice(dic)
            startswith = reply[-1]
            use[reply] = i
            print(i,":私の番です。    ",reply)
        else:
            result = [word for word in dic if word.startswith(startswith) and word not in use]

            if len(result) == 0:
                print("まいりました！　あなたの勝ちです。")
                break
            else:
                reply = choice(result)
                startswith = reply[-1]
                use[reply] = i
                print(i,":私の番です。    ",reply)

print("今回のしりとりでは",len(use),"個の単語を使用しました。")