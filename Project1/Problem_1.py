#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sort(n):                           # Function takes the number of elements in an array
    a = []                             # and sorts it in ascending order.
    aux = []
    
    for i in range(0,n):               # Taking the input of array to be sorted dynamically.
        x =int(input())
        a.append(x)
    
    flag=0;
    
    for i in range(1,n):              # Loop to find the point where the two 
        if a[i] < a[i-1]:             # sub-arrays 'm' and 'n' are sepreated.
            if(i > (n//2)):           
                flag=3;
                temp=i                # when the size of m>n
                break;
            if(i == (n/2)):
                flag=2;              # when the size of m=n
                temp=i
                break;
            else:
                flag=1               # when the size of m<n
                temp=i                
                break;
            
    if(flag==3):
        for i in range(temp,n):         #taking n out of 'a' and storing it in 'aux.'
            aux.append(a[i])
            a.remove(a[i])

    elif(flag==2):
        for i  in range(0,temp):         # taking m out of 'a' and storing it in 'aux.' Also, we 
            aux.append(a[0])             # can take out n as size of both array are equal.
            a.remove(a[0])


    elif(flag==1):
        for i in range(0,temp):
            aux.append(a[0])            # taking m out od 'a' and storing it in 'aux.' 
            a.remove(a[0]) 
    
    elif(flag==0):                    # when 'm' or 'n' is null return the input array.
        return(a)

    for j in range(0,n):
        if(aux[0] < a[j] or aux[0]==a[j]):       # function to sort 'a' and 'aux' and stroing
            a.insert(j,aux[0])                   # the final result in 'a' and printing it.
            aux.remove(aux[0])
            if(len(aux)==0):
                break;
    return(a)
        


# ##### Case-1

# In[2]:


sort(3)


# ##### Case-2

# In[3]:


sort(4)


# ##### Case-3

# In[4]:


sort(8)


# ##### Case-4

# In[5]:


sort(19)

