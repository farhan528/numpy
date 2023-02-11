#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np


# ## Create a 3×3 numpy array of all True’s

# In[11]:


boolean_arr = np.full((3,3), True, dtype=bool)
print(boolean_arr)


# ## Extract all the odd numbers from a numpy array

# In[12]:


odd_numbers = np.array([1,2,3,4,5,6,7,8,9,10,11])
print(odd_numbers[odd_numbers%2!=0])


# ## Replace all odd numbers with -1

# In[13]:


odd_numbers = np.array([1,2,3,4,5,6,7,8,9,10,11])
odd_numbers[odd_numbers%2!=0] = -1
print(odd_numbers)


# ## Stack arrays vertically

# In[15]:


a = np.arange(10).reshape(2,-1)
b = np.repeat(1,10).reshape(2,-1)
print(np.vstack([a,b]))


# ## Stack array horizontally

# In[16]:


a = np.arange(10).reshape(2,-1)
b = np.repeat(1,10).reshape(2,-1)
print(np.hstack([a,b]))


# In[36]:


# input: a = np.array([1,2,3])
# output:  array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

a = np.array([1,2,3])
print(np.r_[np.repeat(a,3), np.tile(a,3)])


# ## Find the common elements b/w two arrays

# In[39]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(a,b))


# ## Remove the common elements b/w two arrays

# In[43]:


a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
print(np.setdiff1d(a,b))


# ## Get the positions where elements of a and b match

# In[53]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a==b)


# ## Get the elements from an array b/w a given range

# In[54]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
index = np.where((a>=5) & (a<=10))
a[index]


# ## Find the pair maximum for every column of two arrays

# In[61]:


def pair_max(a,b):
    c = np.vstack([a,b])
    for col in range(7):
        print(max(c[0:2, col]), end=" ")


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max(a,b)


# ## Swap columns 1 and 2 in the array arr.

# In[66]:


a = np.arange(9).reshape(3,3)
print(a)
print("\nThe swapped array:\n")
print(a[:, [1,0,2]])


# In[ ]:




