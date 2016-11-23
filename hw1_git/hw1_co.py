'''
	Method Combination :


'''

# Import Module
from hw1_fun import *
from placeFeature import *

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

# develop three list to store data
t1 = []
t2 = []
t3 = []

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

ent1 = entropy (t1loc, t1locInfo, t1locVis)
ent2 = entropy (t2loc, t2locInfo, t2locVis)
ent3 = entropy (t3loc, t3locInfo, t3locVis)
'''
print ('T1 : user: %d\tloc: %d\t' % (len(t1uid), len(t1loc)))
print ('T2 : user: %d\tloc: %d\t' % (len(t2uid), len(t2loc)))
print ('T3 : user: %d\tloc: %d\t' % (len(t3uid), len(t3loc)))
'''

timeStop1 = time.time()
print ('Time for preprocessing essential tables : %f' % (timeStop1-timeStart))


# generate two friendship list
f1 = []
f2 = []
f3 = []

for x in t1uid :
	for y in t1uid :
		if x == y : continue
		'''
		minent = min_ent (t1locInfo[x], t1locInfo[y], ent1)
		aaent = aa_ent (t1locInfo[x], t1locInfo[y], ent1)
		'''
		aap = aa_p (t1locInfo[x], t1locInfo[y], t1locVis)
		minp = min_p (t1locInfo[x], t1locInfo[y], t1locVis)

		# Threshold
		#if minent<.6 and minent>.0  and  aaent>4.0:
		if aap>3.0 and minp>0 and minp<6 :
			f1.append ((x, y))

for x in t2uid :
	for y in t2uid :
		if x == y : continue
		'''
		minent = min_ent (t2locInfo[x], t2locInfo[y], ent2)
		aaent = aa_ent (t2locInfo[x], t2locInfo[y], ent2)
		'''

		aap = aa_p (t2locInfo[x], t2locInfo[y], t2locVis)
		minp = min_p (t2locInfo[x], t2locInfo[y], t2locVis)

		# Threshold
		#if minent<.6 and minent>.0  and  aaent>4.0:
		if aap>3.0 and minp>0 and minp<6 :
			f2.append ((x, y))

for x in t3uid :
	for y in t3uid :
		if x == y : continue
		'''
		minent = min_ent (t3locInfo[x], t3locInfo[y], ent3)
		aaent = aa_ent (t3locInfo[x], t3locInfo[y], ent3)
		'''

		aap = aa_p (t3locInfo[x], t3locInfo[y], t3locVis)
		minp = min_p (t3locInfo[x], t3locInfo[y], t3locVis)

		# Threshold
		#if minent<.6 and minent>.0  and  aaent>4.0:
		if aap>3.0 and minp>0 and minp<6 :
			f3.append((x, y))


timeStop2 = time.time()
print ('Time for processing : %f' % (timeStop2-timeStop1))


# combine friendship together (no repeat)
f1 = f1 + f2
friendship = union (f1, f3)


timeStop3 = time.time()
print ('Time for gethering friendship : %f' % (timeStop3-timeStop2))


writeFile (friendship, "method_co.txt")

