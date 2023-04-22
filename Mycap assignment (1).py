#!/usr/bin/env python
# coding: utf-8

# In[1]:



n = int(input("Enter the limit for Fibonacci sequence: "))

a, b = 0, 1


while a < n:
    print(a, end=" ")
    a, b = b, a+b


# In[4]:


list1 = [12, -7, 5, 64, -14]
for i in list1:
    if i>=1:
        print(i,end=' ')


# In[9]:


list2 = [12, 14, -95, 3]
output=[]
for i in list2:
    if i>=1:
        s=i
        output.append(s)
print(output)
        


# In[ ]:




