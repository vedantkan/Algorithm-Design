#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # IF no two elements were swapped by inner loop, then break
        if swapped == False:
            break


arr = [150, 397, 239, 192, 254, 995, 310]
start = time.time()
bubble_sort(arr)

print ("Sorted array :")
for i in range(len(arr)):
    print ("%d" % arr[i], end=" ")

end = time.time()
print("\n\nRuntime of the program is " + str(end - start) + "s.")


# In[ ]:




