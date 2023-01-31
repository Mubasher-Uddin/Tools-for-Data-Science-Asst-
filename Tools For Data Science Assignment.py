#!/usr/bin/env python
# coding: utf-8

# # My Jupyter Notebook on IBM Watson Studio

# ## Name : Shaik Mubasher Uddin

# Data Science 

# Iam intrested in data science because,I enjoy problem-solving,and statistical analysis.

# The Following code displays number of Positives,Negatives, Zero's from a list of number

# In[4]:


lst = [-1,-19,-69,33,25,-99,-45,23,9,-8,0,1,2,-6,0,3]
p,n,z=0,0,0
for i in lst:
    if i>0:
        p=p+1
    elif i<0:
        n=n+1
    else:
        z=z+1
print("Pos=",p)
print("Neg=",n)
print("Zero=",z)


# In[ ]:




