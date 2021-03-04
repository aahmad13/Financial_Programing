#!/usr/bin/env python
# coding: utf-8

# In[1]:


# first import pandas and read html
#once read assign be a variable 
import pandas as pd
url= "https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldYear&year=2021"
df=pd.read_html(url)
df


# In[2]:


# list of DataFrames are returned from read_html() from lecture
for dfs in df:
    print(type(df))
"8 tables are returned for part A1 from using df[]"


# In[3]:


df[1] #bingo we have the interest table


# In[4]:


"index 1 calculate the table of interest rates over time" #answer for the question provided


# In[5]:


#assign a new name to the variable and make a concrete dataframe since this will help you in the long run
#pristing outlook of our data is located in the output
Interest_Rates= df[1]
Interest_Rates=pd.DataFrame(Interest_Rates)
Interest_Rates


# In[6]:


#now set the index with set_index function so that we dont have look from 0:38 row but by the date
Interest_Rates=Interest_Rates.set_index('Date')


# In[7]:


Interest_Rates


# In[8]:


#extract the row using the iloc method referenced the the first few lectures
Latest_Yield=Interest_Rates.iloc[-1]
Latest_Yield


# In[9]:


#input values from the iloc output and assign x as the years and y as the percentage
#notes that the time will be counted for since pandas see the 1/12 as a month/year
time=[1/12,2/12,3/12,6/12,1,2,3,5,7,10,20,30]
yields_in_percents=[0.03,0.03,0.05,0.07,0.08,0.13,0.27,0.71,1.12,1.45,2.11,2.23]
y=yields_in_percents
x=time


# In[10]:


import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.show()


# In[11]:


#select the columns and make them into a dataframe as Year#
Year2=pd.DataFrame(Interest_Rates["2 yr"])
Year10=pd.DataFrame(Interest_Rates["10 yr"])


# In[12]:


#use the line of code provided within the assign to plot each time series along
fig, ax = plt.subplots()
plt.plot("2 yr", data=Year2)
plt.plot("10 yr", data=Year10)
plt.legend()
ax.tick_params(labelbottom=False) # suppress x-axis labels
plt.show()

