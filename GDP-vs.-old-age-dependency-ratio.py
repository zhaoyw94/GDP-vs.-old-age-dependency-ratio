#!/usr/bin/env python
# coding: utf-8

# #  Yiwen Zhao Mini Project
# 

# ## Question : ARB old-age dependency ratio over the years, and what is the relationship between GDP and old-age dependency ratio in ARB?

# In[1]:


import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


# ### let's inport data first 

# In[2]:


data = data = pd.read_csv('./Indicators.csv')


# ### let's create a new dataframe "m" that contains only 'old-age dependency ratio' for the Country ARB
# 

# In[3]:


hist_old = 'Age dependency ratio, old \('
hist_contr = 'ARB'

m1 = data['IndicatorName'].str.contains(hist_old)
m2 = data['CountryCode'].str.contains(hist_contr)

# create a new df to meet above two requirements

m = data[m1 & m2]
m.head(3)


# ### Creating a line chart to illustrate ARB old-age dependency ratio

# In[4]:


# switch to a line plot
plt.plot(m['Year'].values, m['Value'].values)

# Label the axes
plt.xlabel('Year')
# plt.ylabel(stage['IndicatorName'].iloc[0])
plt.ylabel(m['IndicatorName'].iloc[0])
#label the figure
plt.title('ARB old-age dependency ratio')

# to make more honest, start they y axis at 0
plt.axis([1959, 2011,0,25])

plt.show()


# It's clear to see that there was almost no change of old-age dependency ratio between 1960 and 2010 in the ARB

# ## we can also see if there is any relationship between old-age dependency ratio and GDP

# ### Let's create a new dataframe 'ARB_gdp' which is the ARB GDP over the years. 

# In[5]:


# select GDP Per capita emissions for the United States
hist_indicator = 'GDP per capita \(constant 2005'
hist_country = 'ARB'

mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['CountryCode'].str.contains(hist_country)

# stage is just those indicators matching the USA for country code and CO2 emissions over time.
ARB_gdp = data[mask1 & mask2]


# In[6]:


ARB_gdp.head(2)


# In[7]:


ARB_gdp['IndicatorCode'][]


# In[ ]:





# In[ ]:





# In[8]:


# switch to a line plot
plt.plot(ARB_gdp['Year'].values, ARB_gdp['Value'].values)

# Label the axes
plt.xlabel('Year')
plt.ylabel(ARB_gdp['IndicatorName'].iloc[0])

#label the figure
plt.title('GDP Per Capita ARB')

# to make more honest, start they y axis at 0
#plt.axis([1959, 2011,0,25])

plt.show()


# ### ScatterPlot for comparing GDP against old-age dependency ratio emissions (per capita)
# First, we'll need to make sure we're looking at the same time frames 

# In[9]:


print("GDP Min Year = ", ARB_gdp['Year'].min(), "max: ", ARB_gdp['Year'].max())
print("Old ratio Min Year = ", m['Year'].min(), "max: ", m['Year'].max())


# In[10]:


old_ratio_trunc = m[m['Year'] >= 1975]

print("GDP Min Year = ", ARB_gdp['Year'].min(), "max: ", ARB_gdp['Year'].max())
print("Old ratio Min Year = ", old_ratio_trunc['Year'].min(), "max: ", old_ratio_trunc['Year'].max())


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

fig, axis = plt.subplots()
# Grid lines, Xticks, Xlabel, Ylabel

axis.yaxis.grid(True)
axis.set_title('old-age dependency ratio vs. GDP in ARB',fontsize=10)
axis.set_xlabel(ARB_gdp['IndicatorName'].iloc[0],fontsize=10)
axis.set_ylabel(old_ratio_trunc['IndicatorName'].iloc[0],fontsize=10)

X = ARB_gdp['Value']
Y = old_ratio_trunc['Value']

axis.scatter(X, Y)
plt.show()


# In[13]:


np.corrcoef(ARB_gdp['Value'],old_ratio_trunc['Value'])


# Under the trend of aging population, labor supply is declining, social production capacity is insufficient, and economic growth is declining. Second, aging will change the direction of social resources allocation and have an impact on economic growth. Generally speaking, the proportion of the elderly in an aging society is increasing, and the elderly belong to the "consumption-type" population in the economy and do not create output
