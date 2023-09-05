#!/usr/bin/env python
# coding: utf-8

# In[30]:


list_name=[]
list_femal=[]
list_male=[]
n=int(input())
for i in range(n):
    result = str(input())
    list_name.append(result)
for i in list_name:
    x=i.split('.')
    if x[0] =='f':
        gender=x[0]
        names=x[1][0].upper() + x[1][1:].lower()
        programm=x[2]
        z= gender ,names,  programm
        list_femal.append(z)
    if x[0] =='m':
        gender=x[0]
        names=x[1][0].upper() + x[1][1:].lower() 
        programm=x[2]
        y=gender ,names,  programm
        list_male.append(y)

final=list_femal + list_male
j=0
list_name=[]
for f in final:
    
    final_list=f'{final[j][0]} {final[j][1]} {final[j][2]}'
    list_name.append(final_list)
    j+=1
def custom_sort_key(name):
    parts = name.split()
    gender = parts[0]
    language = parts[-1]
    return (gender, language)

sorted_list = sorted(list_name, key=custom_sort_key)

for name in sorted_list:
    print (name)

