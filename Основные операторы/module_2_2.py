#!/usr/bin/python3
first=int(input("first number:"))
second=int(input("second number:"))
third=int(input("third number:"))
cond1=first==second
cond2=second==third
cond3=first==third
if cond1 and cond2 and cond3: print(3)
elif cond1 or cond2 or cond3: print(2)
else: print(0)