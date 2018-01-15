
# coding: utf-8

# # 1. Given two lists L1 = ['a', 'b', 'c'], L2 = ['b', 'd'], find common elements, find elements present in L1  and not in L2?

# In[ ]:


# Import numpy
import numpy as np


# In[2]:


L1 = ['a', 'b', 'c']
L2 = ['b', 'd']


# In[3]:


# Common_elements
common_elements = np.intersect1d(L1, L2)


# In[4]:


# Print common_elements
print(common_elements)


# In[5]:


# Elements in L1 and not in L2?
L1_elements = np.setdiff1d(L1,L2)


# In[6]:


# Print L1_elements
print(L1_elements)


# # 2. How many Thursdays were there between 1990 - 2000?

# In[8]:


# Import numpy
import numpy as np


# In[11]:


# Count num of Thursdays
num_thursdays = np.busday_count('1990', '2000', weekmask = 'Thu')


# In[12]:


# Print num_thursdays
print(num_thursdays)

