#!/usr/bin/env python
# coding: utf-8

# In[1]:



n = int(input("Enter the limit for Fibonacci sequence: "))

a, b = 0, 1


while a < n:
    print(a, end=" ")
    a, b = b, a+b


# In[ ]:




