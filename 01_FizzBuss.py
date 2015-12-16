#!/usr/bin/python
# -*- coding: utf-8 -*-

i=1
num=34

for i in range(1,num+1):
    if(i%5==0):
        if(i%3==0):
            print(i,"FizzBuzz")
        else:
            print(i,"Buzz")
    elif(i%3==0):
        print(i,"Fizz")
    else:
        print(i)