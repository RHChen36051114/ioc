from hw1_fun import *
from placeFeature import *
from globalFeature import *
import sys

argCheck()

data = readFile (sys.argv[1])

uid = getUID (data)

locInfo = getLocInfo (data, uid)

loc = getLoc (data)

lv = locVisit (loc, data)
lvkey = lv.keys()
lvkey.sort()

ent = entropy (lvkey, locInfo, lv)
entkey = ent.keys()
entkey.sort()

homeDict = getHomeLoc (uid, locInfo)
hkey = homeDict.keys()
hkey.sort()


locTable = tableLoc (data)



print ('Home Location :')
for x in hkey :
	print x,
	print ('\t:\t%d' % homeDict[x])
print('====================')

for x in uid :
	for y in uid :
		if x == y : continue

		wdist = w_geodist (x, y, homeDict[x], homeDict[y], locTable, locInfo)

		print ('[%d %d]' % (x,y))
		print ('w_geodist : %f' % wdist)

'''
for x in uid :
	for y in uid :
		if x == y : continue

		minp = min_p (locInfo[x], locInfo[y], lv)
		aap = aa_p (locInfo[x], locInfo[y], lv)

		print ('[%d %d]\t\t' % (x, y))
		print ('min_p : %f' % minp)
		print ('aa_p : %f' % aap)
'''


'''
		aaent = aa_ent (locInfo[x], locInfo[y], ent)
		minent = min_ent (locInfo[x], locInfo[y], ent)

		print ('[%d %d]\t\t' % (x,y))
		print ('aa_ent : %f' % aaent)
		print ('min_ent : %f' % minent)
'''
