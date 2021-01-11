#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib


# In[ ]:


s = smtplib.SMTP("smtp.gmail.com",587)
#security

s.starttls()

s.login("adityabendale@gmail.com","lxnyohrauxzladdf")
for i in range(10):
    msg = input("Enter your message here")
    s.sendmail("adityabendale@gmail.com","adityajoshi733.aj@gmail.com",msg)
s.quit()

