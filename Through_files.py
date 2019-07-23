#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import pandas as pd
import numpy as np
from datetime import datetime

def through_files(origin, destination):
    res = []
    shpfiles = []
    
    for root, dirs, files in os.walk(origin, topdown=True):
        if len(files) > 0:
            res.extend(zip([root]*len(files), files)) # pairs of address-file
        for x in files:
            shpfiles.append(root+"\\"+x)  # full paths saved in the list
            
    sizes = []
    accessedTimes = []
    modificationTimes = []
    metadataTimes = []
    for f in shpfiles:
        statinfo1 = os.stat(f)
        sizes.append(statinfo1.st_size)
        accessedTimes.append(datetime.utcfromtimestamp(statinfo1.st_atime).strftime('%Y-%m-%d %H:%M:%S'))
        modificationTimes.append(datetime.utcfromtimestamp(statinfo1.st_mtime).strftime('%Y-%m-%d %H:%M:%S'))  
        metadataTimes.append(datetime.utcfromtimestamp(statinfo1.st_ctime).strftime('%Y-%m-%d %H:%M:%S'))
    
    #Putting together a dataframe
    df = pd.DataFrame(res, columns=['Path', 'File_Name'])
    df['Full Path'] = df.Path.astype(str).str.cat(df.File_Name.astype(str), sep='\\')
    df['Size, in bytes']=sizes
    df['Last Accessed at'] = accessedTimes
    df['Last Modified at'] = modificationTimes
    df['Last Metadata change at'] = metadataTimes
    
    #Writing in a .csv file
    df.to_csv(destination, index=False)


# In[5]:


through_files(r'C:\Users\us61565\Desktop\Internal',r'C:\Users\us61565\Desktop\Internal\int_test.csv')

