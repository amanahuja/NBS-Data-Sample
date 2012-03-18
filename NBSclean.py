# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 16:48:56 2012

Cleaning up the NBS dataframes
@author: Aman
"""

#Move to working directory
import os
os.chdir('C:\Users\Aman\Documents\Projects\NextBigSound\NBS-Data-Sample')

#Set data directory
datadir = 'data'
path = os.path.join(os.getcwd(), datadir)

from pandas import *

#Retrieve dataframes from the hdf5 file
store = HDFStore(os.path.join(path, 'NBSData.h5'))

'''
Process the dataframes here
'''
pass

#Save the dataframes back into hdf5 file. 

#Close the hdf5 file. 
store.close()