# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 16:18:44 2012

Loading the NBS data into Pandas
@author: Aman
"""

#Move to working directory
import os
os.chdir('C:\Users\Aman\Documents\Projects\NextBigSound\NBS-Data-Sample')

from pandas import *

#Set data directory
datadir = 'data'
path = os.path.join(os.getcwd(), datadir)

masterdf = DataFrame()
#Loop through each file in the data directory
for filename in os.listdir(path):
    #Ignore non-csv files, such as the readme.txt
    if not filename.endswith('csv'): continue

    '''
    For each data file, load the data into a dataframe
    Then concat the file's data into a master dataframe
    '''
    print "Processing file: ", filename

    filepath = os.path.join(path, filename)
    filedata = read_csv(filepath)
    
    #Add to master dataframe
    masterdf = concat([masterdf, filedata])


#Now we have all the data in a one big dataframe
masterdf.columns


''' 
Save the dataframes for future use
'''
store = HDFStore('NBSData.h5')
store['master'] = masterdf
store.close()
