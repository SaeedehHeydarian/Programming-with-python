#!/usr/bin/env python
# coding: utf-8

# In[81]:


n=10
list10=[]
for n in range(n):
    x=int(input())
    list10.append(x)
counter=0
maximum=0 
number=0
def is_prime(x):
    count=0
    for k in range(1, x+1):
        if x % k ==0:
            count+=1
    if count==2:
            return True
    
for i in list10:
    counter=0
    for j in range(1, i+1):
        if (i % j == 0) and (is_prime(j)):
            counter+=1
    
    if counter > maximum :
            maximum=counter
            number=i
print(number, maximum)


# In[82]:





# In[83]:





# In[ ]:





# In[ ]:




