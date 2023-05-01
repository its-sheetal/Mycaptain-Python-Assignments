#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Prompt user to enter the number of terms to generate
n = int(input("Enter the number of terms to generate: "))

# Initialize first two terms of the series
a = 0
b = 1

# Generate Fibonacci sequence
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c


# In[ ]:




