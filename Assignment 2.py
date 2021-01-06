#!/usr/bin/env python
# coding: utf-8

# In[1]:


username = "Aditya603"
password = "qwerty123"
userInput = input("Username: ")
Password = input('Password: ')
a = 0
if userInput == username and Password == password:
    print("Login Successful!")

if userInput != username:
    print("Invalid Username!")
if Password != password:
    while a<5:
        Password = input("Enter password again: ")
        if Password == password:
            print("Login Successful!")
            break
        a+=1
    print("Your account is blocked for 24 hours")


# In[ ]:





# In[ ]:




