#!/usr/bin/env python
# coding: utf-8

# In[2]:


n_terms = int(input("Enter the number of terms you want to generate: "))
num1, num2 = 0, 1
if n_terms <= 0:
   print("Please enter a positive integer")
elif n_terms == 1:
   print("Fibonacci sequence up to", n_terms, "term:")
   print(num1)
else:
   print("Fibonacci sequence:")
   for i in range(n_terms):
       print(num1)
       nth = num1 + num2
       num1 = num2
       num2 = nth


# In[ ]:




