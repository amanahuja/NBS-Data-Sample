# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 16:18:44 2012

Loading the NBS data into Pandas
@author: Aman
"""

#Move to working directory
import os
os.chdir('C:\Users\Aman\Documents\Projects\NextBigSound\NBS-Data-Sample')

#Set data directory
datadir = 'data'
path = os.path.join(os.getcwd(), datadir)

#Loop through each file in the data directory
for filename in os.listdir(path):
    #Ignore non-csv files, such as the readme.txt
    
    '''
    For each data file, load the data into a dataframe
    Then concat the file's data into a master dataframe
    '''
    pass

