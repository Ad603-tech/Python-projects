#!/usr/bin/env python
# coding: utf-8

# In[2]:


#firebase connectivity


# In[20]:


import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("project-2.json")
firebase_admin.initialize_app(cred)
print("Working")


# In[21]:


from firebase_admin import firestore


# In[29]:


db = firestore.client()
doc_ref = db.collection("movies").document("Bollywood")

data = {"Name":["war","kgf","3 idiots","Family-man","Dangal"], "collection":[400,500,200,100,600]}
doc_ref.set(data)
print("done")


# In[24]:


# Retrieve dataset from firebase


# In[32]:


db = firestore.client()
docs = db.collection("movies").stream()

for d in docs:
    #print(d.to_dict())
    database = d.to_dict()


# In[33]:


database["Name"]


# In[34]:


# Guess the movie name


# In[39]:


import random


# In[44]:


movie = database["Name"]
player = input("Write your name: ")
print("Guess the character: ")
print("You have 10 chances to guess the movie name")
print("Best of luck!!", player)


count = 10
guess = ""
word = random.choice(movie)

while count>0:
    fail = 0
    for char in word:
        if char in guess:
            print(char)
        else:
            print("_")
            fail+=1
            
            
    if fail == 0:
        print("Congratulations, you won!!")
        print("The movie name was",word)
        break
    
    g = input("Enter your character: ")
    guess = guess + g
    
    
    if g not in word:
        count = count-1
        print("Wrong Answer:(")
        
        print("You have",count,"more guesses")














# In[ ]:




