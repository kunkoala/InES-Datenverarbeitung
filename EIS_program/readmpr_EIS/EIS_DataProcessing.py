#!/usr/bin/env python
# coding: utf-8

# In[1]:


from galvani import BioLogic
import pandas as pd
import numpy as np
import os
import re


# In[2]:


from galvani import BioLogic
from read_mpr import searchmpr, mpr_pandas, splitToLoops


# In[3]:


regex = re.compile(r'\d+')


# In[4]:


def insertLoopColumn(df):
    # make array first with integer datatype
    a = np.zeros(len(df)).astype(int)

    # insert num of splits below
    split = 36 

    # loopNum
    loopNum = 1

    for index in range(len(a)):
        if index % split == 0 and index != 0:
            loopNum += 1
        a[index] = loopNum

    df.insert(len(df.columns), 'Loop', a)


# In[5]:


def insertCharge(df, filename):
    intsInFilename = [int(x) for x in regex.findall(filename)]
    charge = intsInFilename[1]
    df.insert(len(df.columns), 'C-Rate', charge)


# In[6]:


def batteryStatus(df, filename):  
    stand = [int(x) for x in regex.findall(filename)][-2]
    if stand == 1:
        df.insert(len(df.columns), 'Stand', 0) 
    elif stand == 3:
        df.insert(len(df.columns), 'Stand', 1)


# In[11]:


def mergeDfs(dfs):
    merged = pd.concat(dfs, ignore_index=True)
    return merged


# In[7]:


def selectMeasureColumn(dfs):
    df_selected = []
    for df in dfs:
        df_selected.append(df[['freq/Hz', 'Re(Z)/Ohm', '-Im(Z)/Ohm']])
    return df_selected


# In[8]:


def generateNewColumn(dfs, files):
    df_newcol = selectMeasureColumn(dfs)
    for count, df in enumerate(df_newcol):
        insertCharge(df, files[count])
        insertLoopColumn(df)
        batteryStatus(df, files[count])
    return df_newcol


# In[12]:


def generateNewColumnVar2(dfs, files):
    for count, df in enumerate(dfs):
        insertCharge(df, files[count])
        insertLoopColumn(df)
        batteryStatus(df, files[count])
    return dfs


# In[ ]:




