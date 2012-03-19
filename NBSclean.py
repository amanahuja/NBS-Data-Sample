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
masterdf = store['master']

'''
Process and clean the dataframes
'''
#the good stuff
basicdf = masterdf[['Artist.ID','Day', 'Facebook.fans.d', 'Facebook.fans.t', 'Last.fm.plays.d', 'Last.fm.plays.t', 'MySpace.fans.d', 'MySpace.fans.t',
	'MySpace.plays.d', 'MySpace.plays.t', 'Twitter.fans.d', 'Twitter.fans.t', 'Twitter.statuses.d', 'Twitter.statuses.t', 'YouTube.fans.d', 'YouTube.fans.t',
	'YouTube.plays.d', 'YouTube.plays.t', 'Pandora.fans.d', 'Pandora.fans.t', 'Rdio.fans.d', 'Rdio.fans.t', 'Rdio.plays.d', 'Rdio.plays.t', 'SoundCloud.fans.d',
	'SoundCloud.fans.t', 'SoundCloud.plays.d', 'SoundCloud.plays.t', 'iTunes.Album.Units.d', 'iTunes.Track.Units.d', 'Vevo.plays.d', 'Vevo.plays.t',
	'SiteCatalyst.Visits.d', 'MediaGuide.Radio.Spins.d', 'Spotify.plays.d', 'Wikipedia.views.d']]

    

#Create a multi Index
from datetime import datetime
SECONDS_PER_DAY = 86400

idx_time = basicdf.Day * SECONDS_PER_DAY
idx_time = idx_time.apply(datetime.fromtimestamp)
idx_artist = basicdf['Artist.ID'].apply(int)

idx = MultiIndex.from_tuples(zip(idx_artist, idx_time), 
                             names=['artist','date'])

#Apply the Multi-index
cols = basicdf.columns
rawdata = basicdf.as_matrix()
basicdf = DataFrame(rawdata, columns = cols, index = idx)

#Save the dataframes back into hdf5 file. 
store['basic'] = basicdf

#Close the hdf5 file. 
store.close()
