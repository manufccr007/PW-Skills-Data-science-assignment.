#!/usr/bin/env python
# coding: utf-8

# # Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25.
# 

# In[35]:


def test():
    n=[]
    for i in range(0,25):
        if i%2!=0:
            n.append(i)
    return n


# In[36]:


test()


# # Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to demonstrate their use.
# 

# In[37]:


def test1(*args):
    return args


# In[38]:


test1(1,2,3,4,5,6,[1,2,3,4,5],(5,6,9))


# In[39]:


def test2(**kargs):
    return kargs


# In[40]:


test2(c=32,b=35,d=[1,2,3,6])


# # Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16,18, 20].
# 
# 

# In[41]:


list2=[2,4,6,8,10,12,14,16,18,20]


# In[42]:


list(filter(lambda x: x<11,list2))


# In[ ]:




