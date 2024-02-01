#!/usr/bin/env python
# coding: utf-8

# In[3]:

firstname=[]
coun=0
for i in range(0,5):
    name=input("Enter first name:")
    firstname.append(name)
print(firstname)
for i in firstname:
    coun+=i.count('a')
print("The number of occurance of 'a' in the list is",coun)


# In[ ]:
