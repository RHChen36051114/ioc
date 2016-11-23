'''
Mi : home location => user i has most check-in #

'''
from hw1_fun import (deg2rad, rad2deg, distance)


# ratio of distance of two user's home location & their check-in # at home location
def w_geodist (u1, u2, ml1, ml2, locInfo) :
	if ml1 == ml2 : return .0

	lati1  = ml1[0]
	longi1 = ml1[1]
	lati2  = ml2[0]
	longi2 = ml2[1]

	dis = distance (lati1, longi1, lati2, longi2)

	'''
	c1 = locInfo[u1][ml1]
	c2 = locInfo[u2][ml2]
	
	return dis/float(c1*c2)
	'''
	return dis


# return Home Location dict (lati, longi)
def getHomeLoc (uid, locInfo, locTable) :
	home = {}
	#tmp = []
	lattmp = []
	longtmp =[]

	for x in uid :
		lockey = locInfo[x].keys()
		for y in lockey :
			#tmp.append (locInfo[x][y])
			lattmp.append (locTable[y][0])
			longtmp.append (locTable[y][1])
		lattmp.sort()
		longtmp.sort()

		#home[x] = lockey[tmp.index(min(tmp))]
		#tmp=[]
		home[x] = (lattmp[len(lockey)/2], longtmp[len(lockey)/2])
		lattmp = []
		longtmp = []
	
	return home

