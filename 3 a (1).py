#!/usr/bin/env python
# coding: utf-8

# In[1]:

#list comprehension
list=[]
square=[]
for i in range(0,5):
    n=int(input("Enter integers"))
    list.append(n)
print(list)
square=[i*i for i in list]
print("square list of given list",square)
