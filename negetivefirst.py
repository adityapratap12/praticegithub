# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:26:40 2020

@author: 91788
"""


def negfirst(arr,n):
    j=0
    for i in range (0,n):
        if(arr[i]<0):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j=j+1 
    print(arr)
arr=[] 
n=int(input("enter the value of n"))
for i in range (0,n):
    ese=int(input())
    arr.append(ese)
print("this is the program of the arry of negative number with lest hand side")
negfirst(arr, n)

