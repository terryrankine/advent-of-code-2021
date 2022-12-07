import  numpy as np

import testdata as td

part1 = np.copy(np.pad(td.octo, (1,1), 'constant', constant_values = np.nan))
part2 = np.copy(np.pad(td.octo, (1,1), 'constant', constant_values = np.nan))

#part1
flash = 0
for i in range(1,101):
    #for idxr,row in enumerate(part1):
    part1 = part1 + 1
    #keep going if you find 9's
    while len(np.asarray(np.where(part1 > 9)).T) > 0:
        #for each 9 - flash!
        for coordx, coordy in (np.asarray(np.where(part1 > 9)).T):
            flash +=1
            part1[coordx][coordy] = -99
            part1[coordx-1][coordy-1] += 1
            part1[coordx-1][coordy] += 1
            part1[coordx-1][coordy+1] += 1
            part1[coordx][coordy-1] += 1
            part1[coordx][coordy+1] += 1
            part1[coordx+1][coordy-1] += 1
            part1[coordx+1][coordy] += 1
            part1[coordx+1][coordy+1] += 1

    part1[part1 < 0] = 0
print ('flashcount', flash)



#part2
flash = 0
for i in range(1,10000):
    #for idxr,row in enumerate(part2):
    part2 = part2 + 1
    #keep going if you find 9's
    while len(np.asarray(np.where(part2 > 9)).T) > 0:
        #for each 9 - flash!
        for coordx, coordy in (np.asarray(np.where(part2 > 9)).T):
            flash +=1
            part2[coordx][coordy] = -99
            part2[coordx-1][coordy-1] += 1
            part2[coordx-1][coordy] += 1
            part2[coordx-1][coordy+1] += 1
            part2[coordx][coordy-1] += 1
            part2[coordx][coordy+1] += 1
            part2[coordx+1][coordy-1] += 1
            part2[coordx+1][coordy] += 1
            part2[coordx+1][coordy+1] += 1

    part2[part2 < 0] = 0
   
    if np.nansum(part2)== 0:
        print('simu flash!', i)
        break
            
    