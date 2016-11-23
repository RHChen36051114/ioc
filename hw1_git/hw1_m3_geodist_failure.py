'''
	Method 3 :
		Use Global Feature (w_geodist) to estimate distance weight between users,
		and besides, seperate time to day and night, two time interval.
'''

# Import Module
from hw1_fun import *
from globalFeature import *

import sys
import time


# Read File
argCheck()
data = readFile (sys.argv[1])


timeStart = time.time()

'''
# Establish necessary table
uid			=	getUID (data)
locTable	=	tableLoc (data)
locInfo 	=	getLocInfo (data, uid)
homeDict	=	getHomeLoc (uid, locInfo)
dt			=	decomposeDT (data)
'''

# same as hw1_m2
# change datetime column from string to int list
dt = decomposeDT (data)
d = []
for x in range(len(data)) :
	d.append ((data[x][0], dt[x], data[x][2], data[x][3], data[x][4]))

# develop two list to store day and night data
day = []
night = []

for x in d :
	if x[1][3] > 6 and x[1][3] < 18 :
		day.append(x)
	else :
		night.append(x)


# Establish necessary table apart from day & night
duid = getUID (day)
nuid = getUID (night)
dlocInfo = getLocInfo (day, duid)
nlocInfo = getLocInfo (night, nuid)
dhomeDict = getHomeLoc (duid, dlocInfo)
nhomeDict = getHomeLoc (nuid, nlocInfo)
locTable	=	tableLoc (data)



timeStop1 = time.time()
print ('Time for preprocessing essential tables : %f' % (timeStop1-timeStart))



# generate two friendship list by w_geodist
fsd = []
fsn = []

# day friend
for x in duid :
	for y in duid :
		if x == y : continue

		dwgeodist = w_geodist (x, y, dhomeDict[x], dhomeDict[y], locTable, dlocInfo)	

		# Threshold
		if dwgeodist <= .0 :
			fsd.append ((x, y))


# night friend
for x in nuid :
	for y in nuid :
		if x == y : continue

		nwgeodist = w_geodist (x, y, nhomeDict[x], nhomeDict[y], locTable, nlocInfo)

		# Threshold
		if nwgeodist <= .0 :
			fsn.append ((x, y))



timeStop2 = time.time()
print ('Time for processing w_geodist : %f' % (timeStop2-timeStop1))



# combine friendship together (no repeat)

tmp = fsd + fsn
fs = []

for x in range(len(tmp)) :
	if tmp[x] not in fs :
		fs.append (tmp[x])

#print ('day friend : %d' % len(fsd))
#print ('night friend : %d' % len(fsn))

timeStop3 = time.time()
print ('Time for gethering friendship : %f' % (timeStop3-timeStop2))


writeFile (fs, "method3.txt")

