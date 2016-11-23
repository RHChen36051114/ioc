'''
	Method 6 :
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


# same as hw1_m2
# change datetime column from string to int list
dt = decomposeDT (data)
d = []
for x in range(len(data)) :
	d.append ((data[x][0], dt[x], data[x][2], data[x][3], data[x][4]))

t1 = []
t2 = []
t3 = []

# develop 3 list to store time interval data
# Time split for NY (GMT -5)

for x in d :
	if x[1][3] >= 4 and x[1][3] <= 11 :
		t1.append (x)
	elif x[1][3] >= 12 and x[1][3] <= 19 :
		t2.append (x)
	else :
		t3.append (x)


# Time split for PA (GMT +1)
'''
for x in d :
	if x[1][3] >= 7 and x[1][3] <= 14 :
		t2.append (x)
	elif x[1][3] >= 15 and x[1][3] <= 22 :
		t3.append (x)
	else :
		t1.append (x)
'''

# Time split for SF (GMT -8)
'''
for x in d :
	if x[1][3] >= 7 and x[1][3] <= 14 :
		t1.append (x)
	elif x[1][3] >= 15 and x[1][3] <= 22 :
		t2.append (x)
	else :
		t3.append (x)
'''


# Establish necessary table apart from day & night
t1uid = getUID (t1)
t2uid = getUID (t2)
t3uid = getUID (t3)
t1locInfo = getLocInfo (t1, t1uid)
t2locInfo = getLocInfo (t2, t2uid)
t3locInfo = getLocInfo (t3, t3uid)
t1loc = getLoc (t1)
t2loc = getLoc (t2)
t3loc = getLoc (t3)
t1locVis = locVisit (t1loc, t1)
t2locVis = locVisit (t2loc, t2)
t3locVis = locVisit (t3loc, t3)
locTable = tableLoc (data)
t1homeDict = getHomeLoc (t1uid, t1locInfo, locTable)
t2homeDict = getHomeLoc (t2uid, t2locInfo, locTable)
t3homeDict = getHomeLoc (t3uid, t3locInfo, locTable)


timeStop1 = time.time()
print ('Time for preprocessing essential tables : %f' % (timeStop1-timeStart))


# generate two friendship list by w_geodist
f1 = []
f2 = []
f3 = []


for x in t1uid :
	for y in t1uid :
		if x == y : continue

		#minent = min_ent (t1locInfo[x], t1locInfo[y], ent1)
		#aaent = aa_ent (t1locInfo[x], t1locInfo[y], ent1)

		t1geodist = w_geodist (x, y, t1homeDict[x], t1homeDict[y], t1locInfo)

		# Threshold
		#if minent<.6 and minent>.0  and  aaent>4.0:
		if t1geodist < .1 :
			f1.append ((x, y))

for x in t2uid :
	for y in t2uid :
		if x == y : continue

		#minent = min_ent (t2locInfo[x], t2locInfo[y], ent2)
		#aaent = aa_ent (t2locInfo[x], t2locInfo[y], ent2)

		t2geodist = w_geodist (x, y, t2homeDict[x], t2homeDict[y], t2locInfo)
		
		# Threshold
		#if minent<.6 and minent>.0  and  aaent>4.0:
		if t2geodist < .1 :
			f2.append ((x, y))

for x in t3uid :
	for y in t3uid :
		if x == y : continue

		#minent = min_ent (t3locInfo[x], t3locInfo[y], ent3)
		#aaent = aa_ent (t3locInfo[x], t3locInfo[y], ent3)

		t3geodist = w_geodist (x, y, t3homeDict[x], t3homeDict[y], t3locInfo)

		# Threshold
		#if minent<.6 and minent>.0  and  aaent>4.0:
		if t3geodist < .1 :
			f3.append((x, y))



timeStop2 = time.time()
print ('Time for processing w_geodist : %f' % (timeStop2-timeStop1))



# combine friendship together (no repeat)
f1 = f1 + f2
friendship = union (f1, f3)


timeStop3 = time.time()
print ('Time for gethering friendship : %f' % (timeStop3-timeStop2))


writeFile (friendship, "method6.txt")

