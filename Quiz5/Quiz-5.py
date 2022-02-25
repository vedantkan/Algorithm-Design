#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sys import maxsize
 
def max_subarray_sum(a,size):
 
    max_value = -maxsize - 1
    max_end_val = 0
    start = 0
    end = 0
    s = 0
    
    if(len(a)==0):
        print("Array is empty")
        
    else:

        for i in range(0,size):

            max_end_val += a[i]

            if max_value < max_end_val:
                max_value = max_end_val
                start = s
                end = i

            if max_end_val < 0:
                max_end_val = 0
                s = i+1

        for i in range(start,end+1):
            print(a[i])

        print ("Maximum contiguous sum is ", max_value)


# ##### Case - 1

# In[2]:


a = []
max_subarray_sum(a,len(a))


# ##### Case - 2

# In[3]:


a = [1]
max_subarray_sum(a,len(a))


# ##### Case - 3

# In[4]:


a = [1, 2, 3, 4]
max_subarray_sum(a,len(a))


# ##### Case - 4

# In[5]:


a = [-7,-4,-2,-8]
max_subarray_sum(a,len(a))


# ##### Case - 5

# In[6]:


a = [-2, 3, 5, -7]
max_subarray_sum(a,len(a))


# ##### Case - 6

# In[7]:


a = [-2, -3, 4, -1, -2, 1, 5, -3]
max_subarray_sum(a,len(a))


# ##### Case - 7

# In[8]:


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray_sum(a,len(a))

