import numpy as np
import pandas as pd

def subset(a, n, s,
                    index, temp, i):

    # a is the array
    # n is the length of array a 
    # s is the size of subset required
    # index is the current index of temporary array 
 
    if(index == s):
        for j in range(s):
            print(temp[j], end = " ")
        print(" ")
        return
 

    if(i >= n):
        return

    temp[index] = a[i]
    subset(a, n, s,
                    index + 1, temp, i + 1)
     

    subset(a, n, s, index,
                    temp, i + 1)
    

    

 
 
def getsubset(a, n, s):
 
    temp = list(range(s))
    
    if(s>n):
        print("Subsets cannot be greater than superset")
     

    subset(a, n, s,
                    0, temp, 0)