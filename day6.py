import numpy as np
import testdata as mydata

incoming = np.array(mydata.data)
incoming = np.array(mydata.mydata)

bins = np.bincount(incoming, minlength = 10)
print (incoming)

tomorrow = np.copy(bins)
for day in range(1,257):
    for i in range(0,9):
        tomorrow[i] = bins[i+1]
    tomorrow[6] = bins[0]+bins[7]
    tomorrow[8] = bins[0]
    bins = np.copy(tomorrow)


print (day, tomorrow, sum(tomorrow))
