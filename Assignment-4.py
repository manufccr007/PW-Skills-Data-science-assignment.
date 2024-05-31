#!/usr/bin/env python
# coding: utf-8

# # Question:2

# In[2]:


L=[1,2,3,4,5,6,7,8,9,10]


# In[3]:


list(map(lambda x:x**2,L))


# # Question-3

# In[7]:


L2=[1,2,3,4,5,6,7,8,9,10]
M=list(map(lambda x:str(x),L2))


# In[8]:


N=tuple(M)


# In[9]:


N


# # Question-4

# In[34]:


M1=[i for i in range (0,25)]


# In[38]:


print(M1,end="")


# In[31]:


from functools import reduce


# In[42]:


reduce(lambda x,y:x+y,M1)


# # Question-5

# In[48]:


M5=[2,3,6,9,27,60,90,120,55,46]


# In[49]:


list(filter(lambda x: x if x%2==0 else x%3==0,M5))


# # Question-6

# In[52]:


List2=['python', 'php', 'aba', 'radar', 'level']


# In[54]:


list(filter(lambda x: x==x[::-1],List2))


# In[ ]:




