#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Function is a set of instructrusctions 
# Def is used for defination
# Pass is used in side a function when we want to leave the function body empty
def hello_func():
    pass

print(hello_func())


# In[6]:


def hello_func():
    print('Hello Function')

hello_func()


# In[9]:


# An executed function is equal to the return value
def hello_func():
    return 'Hello Function'

print(hello_func())
print(hello_func().upper())


# In[10]:


def hello_func(greeding):
    return '{}, Function'.format(greeding)

print(hello_func('Hi'))


# In[13]:


def hello_func(greeding, name):
    return '{}, {}'.format(greeding, name)

print(hello_func('Hi', 'Tani'))


# In[ ]:





# In[ ]:





# In[ ]:




