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

		aap = aa_p (locInfo[x], locInfo[y], locVis)
		minp = min_p (locInfo[x], locInfo[y], locVis)

		if aap > 4.0 and minp > 0 and minp < 5 :
			friendship.append((x,y))
'''
		if minp > 0 and minp < 4 :
			friendship.append((x,y))
'''
'''
		if aap > 6.0 :
			friendship.append((x, y))
'''
tStop2 = time.time()
print ('Judge aa_p time : %f' % (tStop2-tStop1))

writeFile (friendship, "method3.txt")

