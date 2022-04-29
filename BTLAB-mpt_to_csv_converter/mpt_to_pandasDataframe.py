#!/usr/bin/env python
# coding: utf-8

# ## BT-LAB .mpt with loops to pandas dataframe

# In[6]:


import pandas as pd
import os


# In[20]:


# this function read the files from the directory of the script
# return the files in the directory

def seekfiles():
    files = []
    for file in os.listdir("."):
        if file.endswith(".mpt"): # take all the files that ends with .mpt format and append the file into the list
            files.append(file)
    return files # return list of files with .mpt format 


# In[8]:


# This function converts the given content of .mpt BT-LAB file into pandas dataset.
# parameter: filecontents --> the contents of the file from readlines()
# return: dataset --> return the dataset as a pandas dataframe

def convertToDataset(filecontents):
    newContent = []
    for lines in filecontents:
        newContent.append(lines.strip()) # delete the spacing \n from each lines
    headerLine = newContent[1][18:] # take the line number of the header in the .mpt file
    tableContent = newContent[int(headerLine)-1] # saved the column values of the data into a list
    header = tableContent.split('\t') # split the tableContent (headers list) from the tabular splitter.
    data = filecontents[int(headerLine):] # take the raw data starting from the header line + 1
    
    newData = [] # the data that is going to be used in making the pandas dataframe,
    for val in data:
        newData.append(val.rstrip().split('\t')) # append each raw data into newData with deleted tabular separator
    df = pd.DataFrame(newData, columns=header) # create a new pandas dataframe using newData list from before.
    dataset = df.apply(lambda x: x.str.replace(',','.')) # replace all comas in data into dots
    dataset = dataset.astype(float) # set all data from string into float
    return dataset 


# In[15]:


# parameter: filecontents --> file content from .readlines
#            dataframe    --> pandas dataframe

def convertLoops(filecontents, dataframe):
    line = None
    
    # find the line where the loop number is located from the filecontent.
    for num, lines in enumerate(filecontents, 1):
        # find loop in the filecontent
        if 'loops' in lines:
            line = num
            
    # take the number of loops string from the .mpt file located in the line variable found above.        
    numLoops = filecontents[line-1][18:] 
    loops = filecontents[line:line+int(numLoops)] # a list of string of the number of loops
    
    # print number of loops
    print('Number of loops: {}'.format(numLoops))
    
    loopStart = [] # -- X ROW -- starting point of new loop (x row) to loop end (y row) in lists
    loopEnd = [] # -- Y ROW -- end point of loop in lists
    
    for line in loops:
        loopStart.append(line.split()[5]) # take the starting point from the string list
    for line in loops:
        loopEnd.append(line.split()[7]) # take the end point from the string list
        
    dataLoops = []
    for i in range(len(loops)):
        # append from row x to row y specified by the loopStart and loopEnd variable above.
        dataLoops.append(dataframe.iloc[int(loopStart[i]):int(loopEnd[i])+1])
    return dataLoops


# In[16]:


# output of seekfiles saved in a list

files = seekfiles()
files


# In[17]:


# convert the files using the defined functions into pandas dataframe.

def toDF(files):
    datasets = []
    for file in files:
        print('Converting to .csv ... \nFilename: {} to .csv'.format(file))
        f = open(file,'r',encoding='ISO-8859-1')
        content = f.readlines()
        datasets.append(convertLoops(content, convertToDataset(content)))
        print()
    return datasets


# In[18]:


dfs = toDF(files)


# In[19]:


# To access a dataframe from the current folder: dfs[x][y] ----> x = database, y = loop index
# example below: 

dfs[0][0]


# In[ ]:





# In[ ]:




