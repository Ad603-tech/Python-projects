#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[8]:


def maximum(a,b,c):
    if a>=b and a>=c:
        greatest = a
    elif b>=a and b>=c:
        greatest = b
    elif c>=a and c>=b:
        greates = c
    return greatest

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("The greatest number is",maximum(a,b,c))


# # Question 2 

# In[13]:


def palindrome(s):
    return s == s[::-1]

s = str(input("Enter anything: "))
ans = palindrome(s)

if ans:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")


# # Question 3

# In[17]:



def numUpperandLower(sentence):
    upper = 0
    lower = 0
    for i in sentence:
        if i>='A' and i<='Z':
            upper+=1
        elif i>='a' and i<='z':
            lower+=1
    print("Number of Upper case letters are: " + str(upper))
    print("Number of Lower case letters are: " + str(lower))


# In[18]:


numUpperandLower("Hello EVERybody")


# # Question 4

# In[33]:



def sumlist(list):
    total = 0
    for j in list:
        total = total + j
    print("The sum of numbers in the list is: ",total)


# In[41]:


sumlist([4,7,8,9])


# # Question 5

# In[47]:


def mullist(list):
    product = 1
    for i in list:
        product *= i
    print("The product of numbers in the list is: ",product)


# In[48]:


mullist([3,6,7,4])


# # Question 6

# In[55]:


def uniquelist(l):
    List1 = list()
    for i in l:
        if i not in List1:
            List1.append(i)
    
    print("Unique list is: ",List1)


# In[56]:


uniquelist([3,3,4,4,6,7,8,9,1,2,3])


# In[ ]:




