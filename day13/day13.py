import testdata as td
import numpy as np

print(td.realfolds)
print (td.dots)

from PIL import Image as im

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=np.inf)

foldedthing = np.copy(td.dots)
for axis,line in td.realfolds:
    print (axis,line)
    if axis == 'y':
        foldedthing = np.copy(foldedthing[0:int(line), :] + np.flip(foldedthing[int(line)+1:,:], axis=0))
    if axis == 'x':
        foldedthing = np.copy(foldedthing[:, 0:int(line)] + np.flip(foldedthing[:,int(line)+1:], axis=1))
foldedthing[foldedthing>0]=1
foldedthing = foldedthing.astype(int)
print (foldedthing)

print (np.count_nonzero(foldedthing))
data = im.fromarray(foldedthing)
data.save('.\\test.png')