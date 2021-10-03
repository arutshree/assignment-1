#!/usr/bin/env python
# coding: utf-8

# In[1]:


numbers=(1,2,3,4,5,6,7,8,9)


# In[2]:


count_odd = 0


# In[3]:


count_even = 0


# In[4]:


for x in numbers:
    if x % 2==0:
        count_even+=1
    else:
        count_odd+=1


# In[5]:


print("number of even numbers:",count_even)
print("number of odd numbers:",count_odd)


# In[ ]:




