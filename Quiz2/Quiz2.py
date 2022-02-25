#!/usr/bin/env python
# coding: utf-8

# In[42]:


def find(mat, srow, erow, scol, ecol, num):

    i = srow + (erow - srow) // 2;
    j = scol + (ecol - scol) // 2;

    
    if (mat[i][j] == num): 
        print("Found " , num , " at [" , i , "," , j,"]");
        


    else:

        if (i != erow or j != scol):
            find(mat, srow, i, j, ecol, num);

        if (srow == erow and scol + 1 == ecol):
            if (mat[srow][ecol] == num):
                print("Found " , num , " at [" , srow , "," , ecol,"]");

        if (mat[i][j] < num):

            if (i + 1 <= erow):
                find(mat, i + 1, erow, scol, ecol, num);

        else:

            if (j - 1 >= scol):
                find(mat, srow, erow, scol, j - 1, num); 
                


# In[43]:


mat1 = [[1,2,3],
        [4,5,6],
        [7,8,9]];
rowcount = 3; colCount = 3; key = 8;

find(mat1, 0, rowcount - 1, 0, colCount - 1, key);


# In[44]:


mat2 = [[2, 4, 9, 14, 14, 15, 18], 
        [21, 27, 31, 35, 42, 45, 50], 
        [54, 59, 64, 69, 82, 84, 84]];
rowcount = 3; colCount = 7; key = 45;
find(mat2, 0, rowcount - 1, 0, colCount - 1, key);


# In[45]:


mat3 = [[3, 15, 21, 24, 83, 87, 88, 93], 
        [178, 319, 541, 669, 770, 793, 848, 970], 
        [1439, 1546, 1853, 2124, 2234, 2459, 2518, 2978],
        [3111, 3406, 3490, 3669, 3796, 3936, 4112, 4776],
        [5277, 5667, 6067, 6555, 7890, 8056, 8234, 9968]];
rowcount = 5; colCount = 8; key = 2356;
find(mat3, 0, rowcount - 1, 0, colCount - 1, key);


# In[ ]:




