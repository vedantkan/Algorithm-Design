#!/usr/bin/env python
# coding: utf-8

# In[1]:


def multiply(num1,num2):            # function to mutiply two number by ala-carte method
    f1=0                            # it takes two numbers as input
    f2=0

    if(num1 <0):
        f1=1                         # creating a flag if num1 or num2 are negetive numbers

    if(num2 <0):
        f2=1

    absnum1 = abs(num1)               # making the numbers positive if they are negetive
    absnum2 = abs(num2)

    finalresult = 0                # intializing a variable to store final result

    while(absnum1 > 0):

        if(absnum1 % 2==1):                          # Adding the corresponding values of absnum2 when 
                                                     # the value of absnum1 is odd
            finalresult = finalresult + absnum2;    

        absnum2 = absnum2*2             # multiplying the absnum2 with 2 until absnum==1

        absnum1 = absnum1//2;           # dividing absnum1 with 2 until its value is equal to 1

    if(f1==1 and f2==1):              # if both numbers are negetive print poistive finalresult

        print(finalresult)

    if(f1==0 and f2==0):               # if both numbers are postive print poistive finalresult
 
        print(finalresult)

    if(f1 != f2):                    # if any number is negetive print negetive finalresult

        print('-',finalresult)


# ##### Case-1

# In[2]:


multiply(7000 , 7294)


# ##### Case-2

# In[3]:


multiply(25 , 5038385)


# ##### Case-3

# In[4]:


multiply(-59724 , 783)


# ##### Case-4

# In[5]:


multiply(8516 , -82147953548159344)


# ##### Case-5

# In[6]:


multiply(45952456856498465985 , 98654651986546519856)


# ##### Case-6

# In[7]:


multiply(-45952456856498465985 , -98654651986546519856)

