# use to operate argv
import sys

# use to read and process check-in data format
import csv

# use to calculate distance with latitude & longitude
from math import cos, sin, acos



# check if user enter input file name
def argCheck () :
    if len(sys.argv) != 2 :
		print ('\n\tUsage :\tpython\t'+sys.argv[0]+'\t(input check-in data)')
		sys.exit()


# read in csv file and return data list
def readFile (filename) :
    with open (filename) as f:
		r = csv.reader (f, delimiter='\t')
		data = [ (int(userID), datetime, float(latitude), float(longitude), int(location)) 
				for (userID, datetime, latitude, longitude, location) in r ]

    f.close()
    return data



# extract uid data from whole data list (no repeat)
def getUID (data) :
    cnt = 1
    uid = [data[0][0]]

    for x in range(len(data)) :
        if x == 0 :
            continue
 
        if uid[cnt-1] == data[x][0] :
            continue
        else :
            uid.append(data[x][0])
            cnt += 1

    return uid



# extract location data from whole data list (no repeat)
def getLoc (data) :
	loctmp = []
	
	for x in data :
		loctmp.append (x[4])

	loc = set(loctmp)
	loc = list (loc)
	loc = sorted (loc)

	return loc


# store dict about location ID to lati & lonti
def tableLoc (data) :
	table = {}
	for x in data :
		if x[4] in table : continue
		table[x[4]] = (x[2],x[3])
	
	return table


# decompose datetime column data from string to 5 parts int list
# ex. '2010-10-20T12:08:15Z'  =>  2010, 10, 20, 12, 08, 15
def decomposeDT (data) :
	dt = []

	for x in range(len(data)) :
		tmpA = data[x][1][:len(data[x][1])-1]	# remove 'Z'
		tmpB = tmpA.split('T')
		tmpC = tmpB[0].split('-') + tmpB[1].split(':')
		tmpD = [int(tmpC[0]), int(tmpC[1]), int(tmpC[2]), int(tmpC[3]), int(tmpC[4]), int(tmpC[5])]
		dt.append (tmpD)

	return dt



# calculate distance of two place by latitude & longitude, 3 functions
# just output kilogram version
pi = 3.14159265358979323846

def deg2rad (deg) :
	return deg * pi / 180

def rad2deg (rad) :
	return rad * 180 / pi

def distance (lat1, lon1, lat2, lon2) :
	theta = lon1 - lon2

	dist = sin(deg2rad(lat1)) * sin(deg2rad(lat2)) + cos(deg2rad(lat1)) * cos(deg2rad(lat2)) * cos(deg2rad(theta))
	dist = acos(dist)
	dist = rad2deg(dist)
	dist = dist * 60 * 1.1515

	# transform dist from mile to kilogram
	dist = dist * 1.609344

	return dist



# extract location data (no repeat) and it's count
def getLocInfo (data, uid) :
	cnt = 0
	idcnt = 0

	loctmp = {}
	locCount = {}

	for x in range(len(data)) :
		# for every user data is scanned, stored location count info in dict type
		if uid[idcnt] != data[x][0] :
			locCount[uid[idcnt]] = loctmp
			loctmp = {}
			idcnt = idcnt + 1

		# store every user's location (no repeat) and it's check-in times
		if data[x][4] in loctmp :
			loctmp[data[x][4]] += 1
		else :
			loctmp[data[x][4]] = 1

		# last line of data, stored in dict anyway
		if x == len(data)-1 :
			locCount[uid[idcnt]] = loctmp

	return locCount



# write list into file
def writeFile (friendship, filename) :
	f = open (filename, "w")

	for x in range(len(friendship)) :
		if x == len(friendship)-1 :
			f.write (str(friendship[x][0]))
			f.write ('\t')
			f.write (str(friendship[x][1]))
			break

		f.write (str(friendship[x][0]))
		f.write ('\t')
		f.write (str(friendship[x][1]))
		f.write ('\n')

	f.close()



# reduce check-in location, if location counts < checkinLimit then remove from locCount
def reduceLocCount (uid, locCount, checkinLimit) :
	locCopy = locCount.copy()

	for x in range(len(locCopy)) :
		locTmp = locCopy[uid[x]].keys()

		for y in range(len(locTmp)) :
			if locCopy[uid[x]][locTmp[y]] < checkinLimit :
				del locCopy[uid[x]][locTmp[y]]

	return locCopy



# (*** function used only in method 1 ***)
# compare all pairs of user, according their "check-in times" & "location match times"
# to judge whether they are friends or not
def compare (uid, locCount, matchLimit) :
	friendship = []
	matchNum = 0

	for x in range(len(uid)) :
		for y in range(len(uid)) :
			if x == y :
				continue

			# compare a pair of user's check-in location match number
			matchSet = set(locCount[uid[x]].keys()) & set(locCount[uid[y]].keys())
			matchNum = len(matchSet)

			if matchNum > matchLimit :
				friendship.append([uid[x], uid[y]])

	return friendship



# store location and it's visitor
def locVisit (loc, data) :
	lv = {}

	# initialize lv[loc] dic
	for x in loc :
		lv[x] = {}

	for x in range(len(data)) :
		if data[x][0] not in lv[data[x][4]].keys() :
			lv[data[x][4]][data[x][0]] = 1
		else :
			lv[data[x][4]][data[x][0]] += 1

	return lv



# union two friendship list
def union (data1, data2) :
	tmp1=[]
	tmp2=[]
	out=[]
	uni=[]

	for x in data1 :
		tmp1.append(str(x[0])+'+'+str(x[1]))
	
	for x in data2 :
		tmp2.append(str(x[0])+'+'+str(x[1]))

	out = tmp1 + tmp2
	out = list(set(out))

	for x in range(len(out)) :
		uni.append(out[x].split("+"))

	return uni

