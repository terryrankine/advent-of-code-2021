import testdata as td

numdays = 100

#createstartSeq
day0={}
for idx in range (len(td.startseq)-1):
    keything = td.startseq[idx:idx+2]
    if  keything in day0:
        day0[keything] += 1
    else:
        day0[keything] = 1

td.days.append(day0)

def counts(pairmapcounts,startstring, endstring):
    elements = {}
    for i in pairmapcounts:
        for letter in i:
            if letter in elements:
                elements[letter] += pairmapcounts[i]
            else:
                elements[letter] = pairmapcounts[i]
    for i in elements:
        if i in startstring or i in endstring:
            elements[i] = (elements[i]-1)//2+1
        else:
            elements[i] = (elements[i])//2
    return elements

for i in range (0,40):
    tomorrow = {}
    #get the list of pairs
    for pair in td.days[i]:
        #for the current pair - get the actions
        for action in td.actionmap[pair]:
            if action in tomorrow:
                tomorrow[action] += td.days[i][pair]
            else:
                tomorrow[action] = td.days[i][pair]
    mystats = counts(tomorrow, td.startseq[0], td.startseq[-1])
    print (i+1, max(mystats.values()), min(mystats.values()))
    td.days.append(tomorrow)
