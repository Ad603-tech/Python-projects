#!/usr/bin/env python
# coding: utf-8

# In[1]:


import onetimepad


# In[2]:


from tkinter import *
# import tkinter

root = Tk()
root.title("Cryptography app")

def encryptMessage():
    a = var.get()
    ct = onetimepad.encrypt(a,"Letsupgrade")
    print("Working",ct)
    
    e2.delete(0,END)
    e2.insert(END,ct)


def decryptMessage():
    a = var2.get()
    ct = onetimepad.decrypt(a,"Letsupgrade")
    print("Working",ct)
    
    e4.delete(0,END)
    e4.insert(END,ct)



l1 = Label(root,text="Plain Text")
l1.grid(row=0,column=0)

var = StringVar()
e1 = Entry(root,textvariable=var)
e1.grid(row=0,column=1)

l3 = Label(root,text="Encrypted Text")
l3.grid(row = 0,column=4)

var2 = StringVar()
e3 = Entry(root,textvariable=var2)
e3.grid(row=0,column=5)

l4 = Label(root,text="Plain Text")
l4.grid(row=1,column=4)



e2 = Entry(root)
e2.grid(row=1,column=1)

b1 = Button(root,text="Encryption",bg = 'yellow',fg='black',command=encryptMessage)
b1.grid(row=2,column=1)

e4 = Entry(root)
e4.grid(row=1,column=5)

l2 = Label(root,text="Encrypted Text")
l2.grid(row=1,column=0)

b2 = Button(root,text="Decryption",bg = 'yellow',fg='black',command=decryptMessage)
b2.grid(row=2,column=5)

root.mainloop()


# In[ ]:




