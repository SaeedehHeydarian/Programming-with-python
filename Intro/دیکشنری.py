#!/usr/bin/env python
# coding: utf-8

# In[90]:


number=int(input())


# In[91]:


dic={}
for i in range(number):
   word=str(input())
   a=word.split()
   dic[a[0]]=a[1:]   
vorodi=input()


# In[92]:


sentence = vorodi.split()
found_key = []


# In[93]:


for word in sentence:
    word_found = False 
    for key, value in dic.items():
        if word in value:
            found_key.append(key)
            word_found = True
            break 
    if not word_found:
        found_key.append(word)
print(" ".join(found_key))

