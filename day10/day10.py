import testdata as td

depth = 0

from collections import deque
totalscore = 0

 
autoscores = []
for sample in td.realdata:
    mystack = deque(sample)
    mytest = deque()
    depth = 0
    error = False
    score = 0
    for idx, i in enumerate (mystack):
        if i in '[{(<':
            mytest.append(i)
            depth += 1
        elif td.pair[i] == mytest[-1]:
            mytest.pop()
            depth += 1
        else:
            print ('Error @ index:', idx, ', got:', i, 'expected :', td.pair[mytest[-1]], 'score:', td.scoredata[i])
            totalscore += td.scoredata[i]
            error = True
            break
    if len(mytest) != 0 and error == False:
        for i in range(len(mytest)):
            currChar = mytest.pop()
            score = 5*score + td.autoscoredata[td.pair[currChar]]
            #print (td.pair[currChar], score)
        autoscores.append(score)
        #print ('\n------------')

print (totalscore)
autoscores = sorted(autoscores)
print (autoscores[len(autoscores)//2])
