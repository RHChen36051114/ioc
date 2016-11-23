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

		woverlap = w_overlap_p (locInfo[x], locInfo[y])
#		overlapp = overlap_p (locInfo[x], locInfo[y])

		if woverlap > .3 :
#		if overlapp > .1 :
			friendship.append((x,y))

tStop2 = time.time()
print ('Judge overlap_p time : %f' % (tStop2-tStop1))

writeFile (friendship, "method3.txt")

