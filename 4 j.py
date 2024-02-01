#!/usr/bin/env python
# coding: utf-8

# In[4]:


dict1={}
for i in range(0,3):
    key=int(input("Enter key:"))
    value=input("Enter a value:")
    dict1[key]=value
print("The first dictionary:",dict1)
dict2={}
for i in range(0,3):
    key=int(input("Enter key:"))
    value=input("Enter a value:")
    dict2[key]=value
print("The second dictionary:",dict2)
dict1.update(dict2)
print("The merged dictionary",dict1)






# In[ ]:
