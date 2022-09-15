#!/usr/bin/env python
# coding: utf-8

# In[26]:


# thanks to echemdata (https://github.com/echemdata/galvani) 
# for source code of converting mpr files to python readable file.


# In[45]:


from galvani import BioLogic
from galvani import MPRfile
import pandas as pd
import os


# In[28]:


# search mpr in current directory.
# can provide filepath and file contains some string
# will use current path if filepath not explicitly given
# will defaultly search for .mpr 
def searchmpr(filepath=".", contains=""):
    files = []
    for file in os.listdir(filepath):
        if file.endswith(".mpr") and contains in file: # take all the files that ends with .mpr format and append the file into the list
            files.append(file)
    return files # return list of files with .mpr format


# In[56]:


# read mpr files in a directory
# if unspecified, dir will be in the same as .py dir
# example below

def readMPR(mprfiles, MPRdirectory="."):
    MPRfiles = []
    for filename in mprfiles:
        MPRfiles.append(BioLogic.MPRfile(MPRdirectory+"/"+filename))
    return MPRfiles


# In[50]:


def convertToPandasDF(mpr_files_list):
    dataframes = []
    for mpr_file in mpr_files_list: 
        if isinstance(mpr_file, MPRfile):
            dataframes.append(pd.DataFrame(mpr_file.data))
    return dataframes 


# In[30]:


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

# usage:
# splitToLoops(dataframe, index)


# In[64]:


### all in one function ###

def mpr_to_pandas(filenames, path):
    df = convertToPandasDF(readMPR(filenames, path))
    return df


# In[ ]:




