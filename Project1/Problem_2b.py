#!/usr/bin/env python
# coding: utf-8

# In[1]:


def lattice(valueA, valueB):                              # funcation taking the 2 numbers to multiply 
                                                          # by the rectangular multiplication method
        
        
    diagonals = [0] * (len(valueA) + len(valueB))
    for indexA, digitA in enumerate(valueA):              # looping over the string to speperate each digit 
        for indexB, digitB in enumerate(valueB):          # of two numbers
            
            value = int(digitA) * int(digitB)             #storing the values of mulitplication of corresponding digits 
            
            diagonals[indexA+indexB+0] += value // 10     # if value grater than 10 storing 10's digit at upper part                         
            diagonals[indexA+indexB+1] += value %  10     # and ones digit in lower part

    digits = []                           # array storing the values 
    rest   = 0                            # varialbe storing the carry over value
    for value in reversed(diagonals):         # Loop to store the values of addition of values 
        value += rest                         # on the cross diagonal of the matrix in 'digits array'
        if value > 9:                       
            rest = value // 10                 # if there is a carry store the floor in rest 
            digits.insert(0, value % 10)       # and take the one's value in the digits array
        else:
            rest = 0                         # if there is not carry store the value directly
            digits.insert(0, value)

    if rest > 0:                    # if the last addition produces carry store the 
        digits.insert(0, rest)      # value of rest at first index

    if digits[0] == 0:            # if the first value of digit is zero ignore it.
        del digits[0]
        
        return digits
    

def test(a,b):
    
    f1=0;                           # creating a flag to check if valueA or valueB is negetive
    f2=0;
    
    """ verifying lattice calculation """
    stringA = str(a)                # converting values to string
    stringB = str(b)
    
    if(stringA[0] == "-"):
        stringA = stringA.replace('-','')          # if stringA is negetive removing the '-' sign
        f1=1
        
    if(stringB[0] == "-"):
        stringB = stringB.replace('-','')        # if stringB is negetive removing the '-' sign
        f2=1

    # python calculates:
    
    resultA = lattice(stringA, stringB)               # calling the funciton to multiply
    resultA = "%s" % (int(stringA) * int(stringB))
    
    if(f1 != f2):                    # if any number is negetive print negetive finalresult
        print("-%s" % (resultA))
    
    if(f1==1 and f2==1):               # if both numbers are negetive print poistive finalresult
        print("%s" % ( resultA))
    
    if(f1==0 and f2==0):              # if both numbers are postive print poistive finalresult
        print("%s" % (resultA))
        


# ##### Case-1

# In[2]:


test(7000 , 7294)


# ##### Case-2

# In[3]:


test(25 , 5038385)


# ##### Case-3

# In[4]:


test(-59724 , 783)


# ##### Case-4

# In[5]:


test(8516 , -82147953548159344)


# ##### Case-5

# In[6]:


test(45952456856498465985 , 98654651986546519856)


# ##### Case-6

# In[7]:


test(-45952456856498465985 , -98654651986546519856)

