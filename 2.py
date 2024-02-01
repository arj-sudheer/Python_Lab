#!/usr/bin/env python
# coding: utf-8

# In[9]:


current=int(input("Enter the current year"))
final=int(input("Enter the final year"))
future=[]
for i in range(current,final+1):
    if(i%4==0 and i%100!=0)or(i%400==0):
        future.append(i);
print("Leap year",future)



# 
# 
# 
