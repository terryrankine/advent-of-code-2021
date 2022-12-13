
import numpy as np

import testdata as data

mydata = np.array(data.data)
myrange = np.ptp(mydata, axis=0)

min = 0
whichNumber = 0
for j in range(0,myrange):
    mysum=0
    for i in mydata:
        mysum += sum(range(0,abs(i-j)+1))
    if min == 0 or min > mysum:
        min = mysum
        whichNumber = j
    



print (min, whichNumber )
