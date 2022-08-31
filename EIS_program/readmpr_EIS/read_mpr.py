#!/usr/bin/env python
# coding: utf-8

# In[14]:


# thanks to echemdata (https://github.com/echemdata/galvani) 
# for source code of converting mpr files to python readable file.


# In[15]:


from galvani import BioLogic
import pandas as pd
import os


# In[16]:


# search mpr in current directory.
def searchmpr():
    files = []
    for file in os.listdir("."):
        if file.endswith(".mpr"): # take all the files that ends with .mpr format and append the file into the list
            files.append(file)
    return files # return list of files with .mpr format


# In[23]:


# convert mpr to pandas dataframe
def convertToPandasDF(mprfiles):
    # if only 1 file
    if isinstance(mprfiles, str):
        mpr_file = BioLogic.MPRfile(mprfiles)
        df = pd.DataFrame(mpr_file.data)
        return df
    
    # multiple files in a list
    mpr_files = []
    for file in mprfiles:
        mpr_files.append(BioLogic.MPRfile(file))
    
    dataframes = []
    for convertedMPR in mpr_files:
        dataframes.append(pd.DataFrame(convertedMPR.data))
    return dataframes


# In[24]:


def mpr_pandas(files):
    dfs = convertToPandasDF(files)
    return dfs

# In[25]:

def splitToLoops(df, indexToSplit):
    dataframes = []
    splits = int(len(df)/indexToSplit)
    start = 0
    end = indexToSplit
    for split in range(splits):
        temporary_df = df.iloc[start:end]
        dataframes.append(temporary_df)
        start += indexToSplit
        end += indexToSplit
    return dataframes




