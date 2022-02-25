#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


# In[2]:


def bcd(n, k):
    B = [[0 for x in range(k+1)] for x in range(n+1)]
 
    for i in range(n+1):
        for j in range(min(i, k)+1):
  
            if j == 0 or j == i:
                B[i][j] = 1
 
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]
 
    return B[n][k]


# In[61]:


n = 2250
t = []
k = []


# In[62]:


for i in range(0,2250,10):
    start = time.time()
    coef = bcd(n,i)
    end = time.time()
    elapsed = end - start
    t.append(elapsed)
    k.append(i)


# In[63]:


sns.lineplot(k,t)


# In[64]:


k1 = 500
t1 = []
n1 = []


# In[65]:


for i in range(490,2000,10):
    start = time.time()
    coef = bcd(i,k1)
    end = time.time()
    elapsed = end - start
    t1.append(elapsed)
    n1.append(i)


# In[66]:


sns.lineplot(n1,t1)


# In[ ]:




