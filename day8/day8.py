from testdata import *

output = []
for line in data.split('\n'):
    output += [line.split('|')[1].strip().split(' ')]

total = 0
for idx, i in enumerate(output):
    for idx2, j in enumerate(i):
        i[idx2] = ''.join(sorted(j))
    output[idx] = i

        
for idx, i in enumerate(output):
    for idx2, j in enumerate(i):
        length = len(j)
        if length == 2 or \
            length == 3 or \
            length == 4 or \
            length == 7:
            total += 1
    

print (output)
print (total)

output = []
for line in data.split('\n'):
    print (line)
    output += [line.split('|')[0].strip().split(' ')]
total = 0
for idx, i in enumerate(output):
    for idx2, j in enumerate(i):
        i[idx2] = ''.join(sorted(j))
    output[idx] = i
print (output)
print (lookupMap)
