#!/usr/bin/env python
# coding: utf-8

# In[5]:


dict1={}
for i in range(0,4):
    key=input("Enter key:")
    value=input("Enter  value:")
    dict1[key]=value
print("Dictionary in ascending order:",dict(sorted(dict1.items())))
print("Dictionary in descending order:",dict(sorted(dict1.items(),reverse=True)))




# In[ ]:
