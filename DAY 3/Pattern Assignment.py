#!/usr/bin/env python
# coding: utf-8

# In[4]:


n = int(input("Enter the number: "))
for row in range(n):
    for col in range(n,row,-1):
        print("*",end=" ")
    print()


# In[ ]:




