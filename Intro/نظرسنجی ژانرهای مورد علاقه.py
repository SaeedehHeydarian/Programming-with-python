#!/usr/bin/env python
# coding: utf-8

# In[14]:


Genres={"Horror":0, "Romance":0, "Comedy":0, "History":0, "Adventure":0 , "Action":0}
n=int(input())
movie_list=[]
for i in range(n):
    input_movie=input()
    movie_list.extend(input_movie.split(" "))
for genre in movie_list:
    if genre in Genres:
        Genres[genre]+=1

sorted_genres =sorted(Genres.items(), key=lambda x: (-x[1], x[0]))
Dictionary=dict(sorted_genres)


for keys , values in Dictionary.items():
    print(f"{keys} : {values}")


# In[ ]:




