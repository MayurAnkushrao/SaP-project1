#!/usr/bin/env python
# coding: utf-8

# # import libraries

# In[7]:


import pandas as pd


# In[8]:


import seaborn as sns


# In[9]:


df = pd.read_csv("TWO_CENTURIES_OF_UM_RACES.csv")


# In[10]:


df.head(10)


# In[11]:


df.shape


# In[12]:


df.dtypes


# # clean up data

# In[13]:


#Only want USA Races, 50k or 50Mi, 2020


# In[14]:


df[df['Event distance/length']== '50mi']


# In[15]:


df[df['Event distance/length'].isin(['50km','50mi'])]


# In[16]:


df[df['Event distance/length'].isin(['50km','50mi'])    &  (df['Year of event'] == 2020 )]


# In[17]:


df[df['Event name']=='Everglades 50 Mile Ultra Run (USA)']['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)


# In[29]:


#combine all filters


# In[33]:


df[df['Event distance/length'].isin(['50km','50mi'])    &  (df['Year of event'] == 2020 )  &  (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)=='USA')]


# In[34]:


df2 = df[df['Event distance/length'].isin(['50km','50mi'])    &  (df['Year of event'] == 2020 )  &  (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)=='USA')]


# In[35]:


df2.head(10)


# In[36]:


df2.shape


# In[ ]:


#remove USA from events name


# In[37]:


df2['Event name'].str.split('(').str.get(0)


# In[38]:


df2['Event name']=df2['Event name'].str.split('(').str.get(0)


# In[39]:


df2.head()


# In[ ]:


#clean up athelete age


# In[40]:


df2['athlete_age'] = 2020 - df2['Athlete year of birth']


# In[ ]:


#remove h from athlete performance


# In[44]:


df2['Athlete performance'] =df2['Athlete performance'].str.split(' ').str.get(0)


# In[45]:


df2.head(5)


# In[46]:


#drop colomns: Athelete Club,Athelete Contry, Athelete year of birth, Athelete age categery


# In[47]:


df2=df2.drop(['Athlete club','Athlete country','Athlete year of birth','Athlete age category'], axis=1)


# In[48]:


df2.head()


# In[49]:


#clear up null values


# In[50]:


df2.isna().sum()


# In[52]:


df2[df2['athlete_age'].isna()==1]


# In[53]:


df2=df2.dropna()


# In[54]:


df2.shape


# In[55]:


df2[df2.duplicated()==True]


# In[56]:


#reset index


# In[57]:


df2.reset_index(drop=True)


# In[ ]:


#fix types


# In[58]:


df2.dtypes


# In[59]:


df2['athlete_age']=df2['athlete_age'].astype(int)


# In[61]:


df2['Athlete average speed']=df2['Athlete average speed'].astype(float)


# In[62]:


df2.dtypes


# In[63]:


df2.head()


# In[ ]:


#rename colomns
#Year of event                  int64
#Event dates                   object
#Event name                    object
#Event distance/length         object
#Event number of finishers      int64
#Athlete performance           object
#Athlete gender                object
#Athlete average speed        float64
#Athlete ID                     int64
#athlete_age                    int32
#dtype: object


# In[65]:


df2=df2.rename(columns={'Year of event':'year',
                        'Event dates':'race_day',
                        'Event name':'race_name',
                        'Event distance/length ':'race_length',
                        'Event number of finishers':'race_number_of_fnishers',
                        'Athlete performance':'athlete_performance',
                        'Athlete gender':'athlete_gender',
                        'Athlete average speed':'athlete_average_speed',
                        'Athlete ID':'athlete_id'
})


# In[66]:


df2.head()


# In[67]:


df2[df2['race_name']=='Everglades 50 Mile Ultra Run ']


# In[71]:


sns.histplot(df2['Event distance/length'])


# In[74]:


sns.histplot(df2, x='Event distance/length',hue='athlete_gender')


# In[76]:


sns.displot(df2[df2['Event distance/length']=='50mi']['athlete_average_speed'])


# In[81]:


sns.violinplot(data=df2,x='Event distance/length' , y='athlete_average_speed')


# In[82]:


sns.violinplot(data=df2,x='Event distance/length' , y='athlete_average_speed', hue='athlete_gender') 


# In[83]:


sns.violinplot(data=df2,x='Event distance/length' , y='athlete_average_speed', hue='athlete_gender', split=True, inner='quartz')


# In[87]:


sns.lmplot(data=df2,x='athlete_age',y='athlete_average_speed')


# In[88]:


sns.lmplot(data=df2,x='athlete_age',y='athlete_average_speed',hue='athlete_gender')


# In[ ]:


#Diffrence in speed for the 50k, 5mi male to female


# In[91]:


df2.groupby(['Event distance/length','athlete_gender'])['athlete_average_speed'].mean()


# In[ ]:


#what age groups are the best in the 50m Race(20+races min)


# In[95]:


df2.query('`Event distance/length`=="50mi"').groupby('athlete_age')['athlete_average_speed'].agg(['mean','count']).sort_values('mean',ascending=False).query('count>19')


# In[ ]:


#what age groups are the worst in the 50m Race(20+races min)


# In[96]:


df2.query('`Event distance/length`=="50mi"').groupby('athlete_age')['athlete_average_speed'].agg(['mean','count']).sort_values('mean',ascending=True).query('count>19')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




