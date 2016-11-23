from hw1_fun import *
from placeFeature import *

import sys
import time


argCheck ()
data = readFile (sys.argv[1])

tStart = time.time()

uid = getUID (data)
loc = getLoc (data)
locInfo = getLocInfo (data, uid)
locVis = locVisit (loc, data)

ent = entropy (loc, locInfo, locVis)

tStop1 = time.time()
print ('Preprocessing time : %f' % (tStop1-tStart))

friendship=[]
for x in uid :
	for y in uid :
		if x == y : continue

		minent = min_ent (locInfo[x], locInfo[y], ent)

		aaent = aa_ent (locInfo[x], locInfo[y], ent)

		#print('%f' % minent)
		if minent < .6 and minent > .0 and aaent > 5.0 :
			friendship.append((x, y))

tStop2 = time.time()
print ('Judge min_ent time : %f' % (tStop2-tStop1))

writeFile (friendship, "method3.txt")

