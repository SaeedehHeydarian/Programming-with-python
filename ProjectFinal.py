#!/usr/bin/env python
# coding: utf-8

# In[523]:


import requests
import numpy as np
from datetime import date
import re
import datetime
from bs4 import BeautifulSoup
import mysql.connector
import pandas as pd
from decimal import Decimal
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler , OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression


# In[434]:


Dataset=[]
for i in range(1 , 200):
    url="https://iranfile.ir/properties/buy-apartment?page="+str(i)
    r=requests.get(url)
    soup=BeautifulSoup(r.content , "html.parser")
    for i in range(20):
        houses=soup.find_all("tr" , {"data-index":str(i)})
        for p in houses:
            area=p.find("td" , {"data-title":"زیربنا"}).text
            floor=p.find("td" , {"data-title":"طبقه"}).text
            age_build=p.find("td" , {"data-title":"سن بنا"}).text
            date_=p.find("td" , {"data-title":"تاریخ"}).text
            date=re.sub(r'/', '-', date_)
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
            formatted_date = date_obj.strftime('%Y-%m-%d')
            addres=(p.find("td" , {"data-title":"آدرس"}).text).split()
            add=addres[0:2]
            address=add[0].strip()
            Price =re.sub( "\\n" , "" , p.find("td" , {"data-title":"قیمت کل"}).text).strip()
            Dataset.append([area ,floor ,age_build ,formatted_date, address, Price])
          


# In[ ]:


mydb = mysql.connector.connect(
    host="your_host",
    user="your_user",
    password="your_password",
    database="your_database")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE mytable(area VARCHAR(20) ,floor VARCHAR(20) ,age_build VARCHAR(20) ,date VARCHAR(20), address VARCHAR(20), Price VARCHAR(20))
mydb.commit()

for area ,floor ,age ,date, address, Price in Dataset:
        query = "INSERT INTO mytable (area ,floor ,age_build ,date, address, Price) VALUES (%s, %s ,%s, %s,%s, %s )"
        values = (area ,floor ,age_build ,date, address, Price)
        mycursor.execute(query, values)
        mydb.commit()

mydb.close()  


# In[ ]:


select_query = "SELECT * FROM your_table"
mycursor.execute(select_query)
Dataset = mycursor.fetchall()
mycursor.close()
mydb.close()


# In[483]:


df = pd.DataFrame(Dataset, columns=["area" ,"floor" ,"age_build" ,"date", "address", "Price" ] , index=None)
df.head()


# In[484]:


columns=["area" , "age_build" , "floor" ]

for col in columns:
    df[col] = pd.to_numeric(df[col] , errors='coerce')


# In[485]:


df = df.dropna(subset=['floor'])


# In[486]:


df['floor'] = df['floor'].astype(int)


# In[487]:


df['Price'] = df['Price'].str.replace(',', '').astype(np.int64)


# In[488]:


df["address"]=df["address"].str.strip()


# In[489]:


values_to_drop = ['تهران', 'شهر', 'بلوار' , 'شهرك' , 'خ','سی']


# In[490]:


df = df[~ df['address'].isin(values_to_drop)]


# In[491]:


df_reset = df.reset_index()


# # Train

# In[494]:


y=df_reset["Price"]


# In[495]:


x=df_reset.drop(columns=["Price" , "index"] , axis=1)
x.head()


# In[496]:


X_train, X_test , y_train , y_test=train_test_split(x , y , test_size=0.2 , random_state=42)


# In[501]:


pip=Pipeline([
   ( "std" , StandardScaler())
])
num_feature=list(["area" , "age_build" , "floor"])
cat_feature=list(["date" , "address"])


# In[502]:


full_pip=ColumnTransformer([
    ("num" ,pip ,num_feature  ),
    ("cat" , OneHotEncoder() ,cat_feature )
])


# In[503]:


x_train=full_pip.fit_transform(X_train)


# In[504]:


lr=LinearRegression()


# In[505]:


lr.fit(x_train , y_train)


# In[512]:


some_data=x.iloc[:5]
some_label=y.iloc[:5]
pre_some_data=full_pip.transform(some_data)


# In[519]:


print(some_label)
lr.predict(pre_some_data)

