import testdata as td

import numpy as np
from scipy.signal import argrelextrema

sum = 0
rowset = set()
for idx, row in enumerate(td.sampledata):
    for loc in [argrelextrema(row, np.less)]:
        if len(loc[0]) > 0:
            for i in loc[0]:
                rowset.add((idx, i))

colset=set()

for idx, col in enumerate(td.sampledata.T):
    for loc in [argrelextrema(col, np.less)]:
        if len(loc[0]) > 0:
            for i in loc[0]:
                colset.add((i, idx))


for i,j in rowset.intersection(colset):
    sum += td.sampledata[i][j] + 1
print (sum)



#part 2
from pylab import *
from scipy.ndimage import label, sum


#masking - 9s = borders, but ndimage uses 0 as boundaries....
td.sampledata = td.sampledata.astype(float)
for idx, row in enumerate(td.sampledata):
    td.sampledata[idx][td.sampledata[idx] == 9] = -1
    td.sampledata[idx][td.sampledata[idx] == 0] = 1
    td.sampledata[idx][td.sampledata[idx] == -1] = 0


#generate clusters
lw, num = label(td.sampledata)

#make the data all 1 - each element is worth 1 unit
for idx, row in enumerate(td.sampledata):
    td.sampledata[idx][td.sampledata[idx] != 0] = 1
    
#using the clusters as the array index = add the values (which are 1)
area = sum(td.sampledata, lw, index=arange(lw.max()+1))

#get the top 3
area = sorted(area)
print (area.pop() * area.pop() * area.pop())