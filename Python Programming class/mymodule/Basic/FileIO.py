#!/usr/bin/env python
# coding: utf-8

# In[1]:


def open_file(path):
    myf = open(path,encoding = "utf-8")
    txt = myf.read()
    myf.close()
    return txt


# In[2]:


def save_file(path,cnt):
    myf = open(path, "w",encoding="utf-8")
    myf.write(cnt)
    myf.close()


# In[3]:


print(open_file('D:\Python_class\python installation guide.txt'))


# In[ ]:




