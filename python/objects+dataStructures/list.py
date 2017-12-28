'''
Title : Lists
Subdomain: Data Types
Domain: python
Author: Jean Njoroge
Created : August 23rd 2017
'''
ar = []
n=int(input())
for i in range(0,n):
    tmp_str=input()
    tmp_str_ar=tmp_str.strip().split(" ")
    cmd=tmp_str_ar[0]

if(cmd=="print"):
        print(ar)

elif(cmd=="sort"):
        ar.sort()
