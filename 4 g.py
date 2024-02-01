#!/usr/bin/env python
# coding: utf-8

# In[5]:


colorlist1=input("Enter the first list of colors")
color_list1=colorlist1.split(",")
print("First list of colors",color_list1)
colorlist2=input("Enter the second list of colors")
color_list2=colorlist2.split(",")
print("second list of colors",color_list2)
diff=set(color_list1)-set(color_list2)
print("Colors from color_list1 not contained in color_list2",diff)




# In[ ]:
