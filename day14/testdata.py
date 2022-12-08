days = []

startseq = 'NNCB'
startseq = 'OFSNKKHCBSNKBKFFCVNB'


actions = '''CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''.splitlines()

actions = '''KC -> F
CO -> S
FH -> K
VP -> P
KF -> S
SV -> O
CB -> H
PN -> F
NC -> N
BC -> F
NP -> O
SK -> F
HS -> C
SN -> V
OP -> F
ON -> N
FK -> N
SH -> B
HN -> N
BO -> V
VK -> H
SC -> K
KP -> O
VO -> V
HC -> P
BK -> B
VH -> N
PV -> O
HB -> H
VS -> F
KK -> B
HH -> B
CF -> F
PH -> C
NS -> V
SO -> P
NV -> K
BP -> N
SF -> V
SS -> K
FP -> N
PC -> S
OH -> B
CH -> H
VV -> S
VN -> O
OB -> K
PF -> H
CS -> C
PP -> O
NF -> H
SP -> P
OS -> V
BB -> P
NO -> F
VB -> V
HK -> C
NK -> O
HP -> B
HV -> V
BF -> V
KO -> F
BV -> H
KV -> B
OF -> V
NB -> F
VF -> C
PB -> B
FF -> H
CP -> C
KH -> H
NH -> P
PS -> P
PK -> P
CC -> K
BS -> V
SB -> K
OO -> B
OK -> F
BH -> B
CV -> F
FN -> V
CN -> P
KB -> B
FO -> H
PO -> S
HO -> H
CK -> B
KN -> C
FS -> K
OC -> P
FV -> N
OV -> K
BN -> H
HF -> V
VC -> S
FB -> S
NN -> P
FC -> B
KS -> N'''.splitlines()

actionmap = {}
for line in actions:
    orig, new = line.split(' -> ')
    actionmap[orig] = [orig[0]+new,new+orig[1]]
    
print (actionmap)

testday = ['NNCB', 'NCNBCHB', 'NBCCNBBBCBHCB', 'NBBBCNCCNBBNBNBBCHBHHBCHB', 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB']
