#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


# ### Case-1 *n* constant and *k* variable

# In[2]:


def bc(n, k):
 
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    return bc(n-1, k-1) + bc(n-1, k)


# In[12]:


n = 30
t = []
k = []


# In[13]:


for i in range(0,30,1):
    start = time.time()
    coef = bc(n,i)
    end = time.time()
    elapsed = end - start
    t.append(elapsed)
    k.append(i)


# In[18]:


sns.lineplot(k,t)


# ### Case-2 *k* constant and *n* variable

# In[40]:


k1 = 10
t1 = []
n1 = []


# In[42]:


for i in range(5,30,1):
    start = time.time()
    coef = bc(i,k1)
    end = time.time()
    elapsed = end - start
    t1.append(elapsed)
    n1.append(i)


# In[43]:


sns.lineplot(n1,t1)


# In[ ]:




