#!/usr/bin/env python
# coding: utf-8

# In[ ]:


vorodi=str(input())
words=vorodi.split()
count=0
list_capital=[]
list_index=[]
for index , word in enumerate(words , start=1):
    kalame=word.rstrip(",.")
    if (kalame[0].isupper())  and  (index==2 or words[index - 2][-1] != '.') and not kalame.isdigit():
        list_capital.append(kalame)
        list_index.append(index)
if len(list_capital)==0:
    print("None")
else:
    for i , w in zip(list_index ,list_capital ):
        print(f"{i}:{w}")


# In[ ]:





# In[ ]:





# In[ ]:




