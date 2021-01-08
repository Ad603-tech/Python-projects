#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[10]:


List = list()
n1 = int(input("Enter the size of the list:"))
print("Enter the elements of the list:")
for i in range(n1):
    k = input("")
    List.append(k)
print(set(List))


# # Question 2

# In[7]:


def Diff(A,B):
    D = list(set(A)-set(B))
    print('Difference between two list',D)
    return


A = list()
n = int(input("Enter the size of list:"))
print("Enter the elements of first list:")
for i in range(n):
    k = input("")
    A.append(k)

B = list()
m = int(input("Enter the size of list:"))
print("Enter the elements of second list:")
for i in range(m):
    k = input("")
    A.append(k)

print(Diff(A,B))


# # Question 3

# In[16]:



W = list()
m = int(input("Enter the size of list:"))
print("Enter the elements of the list:")
for i in range(m):
    k = input("")
    W.append(k)
frequency = {}
for item in W:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item] = 1

print("Frequency of each element is",frequency)






# # Question 4

# In[19]:


Color1 = ["red","orange","green","blue","white"]
Color2 = ["black","yellow","green","blue"]
D1 = list(set(Color1)-set(Color2))
print("Color1-Color2:",D1)
D2 = list(set(Color2)-set(Color1))
print("Color2-Color1:",D2)


# # Question 5

# In[24]:


def find_longest_word(words_list):  
    word_len = []  
    for n in words_list:  
        word_len.append((len(n), n))  
    word_len.sort()  
    return word_len[-1][1]  
  
w = list()
m = int(input("Enter the size of list:"))
print("Enter the elements of the list:")
for i in range(m):
    k = input("")
    w.append(k)

print("The longest word in the list is",find_longest_word(w))


# # Question 6

# In[4]:


print("Enter a line of text: ")
line = input("")
counts = dict()
words = line.split()
for word in words:
    counts[word]=counts.get(word,0)+1
print("Counts",counts)


# # Question 7

# In[7]:


Text = input("Enter a line of text: ")
vowels = 'aeiou'
count = {}.fromkeys(vowels,0)
for char in Text:
    if char in count:
        count[char]+=1
print(count)


# # Question 8

# In[2]:


n = int(input("Enter a number: "))
d = dict()

for i in range(1,n+1):
    d[i]=i*i
    
print(d)
    


# # Question 9

# In[4]:


from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d3 = Counter(d1)+Counter(d2) 

print(d3)


# # Question 10

# In[5]:


L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)


# In[ ]:




